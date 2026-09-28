# USB DFU bootloaders and DFU programming flows

USB DFU (Device Firmware Upgrade, USB class 0xFE/0x01) lets a host tool (`dfu-util`,
`openFPGALoader --dfu`) write a bitstream into a board's SPI flash over plain USB,
without a JTAG cable. On FPGA boards, the USB device doing this is either **gateware**
(a small SoC loaded from flash at power-on that enumerates as DFU and then hands over
to the user bitstream) or a **companion MCU** (RP2040, STM32, ESP32-S3).

Reviewed 2026-09-28 from the clones pinned in `.claude/memory/sources.tsv`. Paths are
relative to `original_sources/<slug>/` and cite the short pinned commit. Prebuilt images
(`.dfu`, `.bit`, `.img`) were not run or disassembled. Some were pruned locally, and
`emard__ulx3s-bin/fpga/dfu/*/multiboot.img.gz` is still present but was not inspected.
`unknown` means not verified in the cloned source.

## Summary: DFU bootloader implementations

"Kind" means: **gateware + soft CPU** (the USB DFU class runs as firmware on a soft CPU
inside the FPGA), **gateware runtime only** (the user design only supports DFU *detach*,
and the bootloader is elsewhere), or **MCU** (DFU is not done by the FPGA).

| Implementation | Source in this collection | Board / FPGA | Kind | USB core | VID:PID (DFU mode) | Alt settings | Flash layout / hand-off | License | Build |
|---|---|---|---|---|---|---|---|---|---|
| **ULX3S DFU bootloader** (emard fork of HAD2019 badge bootloader) | `emard__had2019-playground/projects/bootloader/` @ 0723f2a | ULX3S v2.0/v3.0.x, v3.1.4, v3.1.7 (12F–85F); ULX4M | gateware + soft CPU (PicoRV32, firmware in BRAM) | early ECP5 variant of no2usb (`cores/usb/rtl/`) | `1d50:614b` | 0–5 (+ RTC zone in table only, see below) | bootloader `0x000000–0x1FFFFF`, user bitstream at `0x200000`; hand-off by pulling PROGRAMN, bootloader packed with `--bootaddr 0x200000` | per file: RTL BSD-3, firmware + USB core LGPL-3.0+, `picorv32.v` ISC | yosys + nextpnr-ecp5 + ecpbram + ecppack + ecpmulti; `riscv-none-embed-gcc` |
| **Hazard3-Doom vendored copy** (ULX4M-LD validated) | `ulx3s__hazard3-doom/bootloader/` @ 4262159 | ULX4M-LD v0.0.3, LFE5UM-85F (also keeps ULX3S tops) | same as above | same | `1d50:614b` | 0–5 | same | same, provenance in `LICENSES/HAD2019-Bootloader-NOTICE.md` | same; self-contained (`mk/`, `cores/` vendored) |
| HAD2019 badge bootloader (the original) | not cloned (smunaut/had2019-playground). Layout documented in `spritetm__hadbadge2019_fpgasoc/doc/programming-storage.md` @ 6e706d5 | Hackaday Supercon 2019 badge, ECP5 45F (unverified) | gateware + soft CPU | no2usb (ECP5) | Makefiles accept `1d50:614a,1d50:614b` (`soc/Makefile:204`) | 0 SoC, 1 IPL, 2 cart…, 5 bootloader | bootloader `0–0x17FFFF`, SoC bitstream `0x180000`; hand-off via PROGRAMN | unknown (not cloned) | unknown |
| ECP5-Mini fork | not cloned (joshajohnson/had2019-playground, branch `ecp5-mini`), referenced in `joshajohnson__ecp5-mini-projects/README.md:13` @ 4e86228 | ECP5 Mini (12F default) | gateware + soft CPU (inferred from fork, unverified) | unknown | `1d50:614b` (`verilog/common.mk:46`) | 0 = user | user at `0x180000` (`common.mk:37-38`) | unknown | unknown |
| **no2bootloader** (Nitro) | bootloader not cloned (no2fpga/no2bootloader). Its DFU class firmware lives in `smunaut__ice40-playground/cores/no2usb/fw/v0/src/usb_dfu.c` (submodule @ d359102) | iCE40 UP5K: iCEBreaker-bitsy, reDIP-SID, icE1usb | gateware + soft CPU (unverified for the bootloader itself) | no2usb | `1d50:6146` (iCEBreaker-bitsy), `1d50:6156` / `6159` (reDIP-SID), `1d50:6144` (icE1usb) | 0 = iCE40 bitstream, 1 = RISC-V firmware | multi-image iCE40 flash, hand-off via `SB_WARMBOOT` (image numbers unknown) | no2usb: HDL CERN-OHL-P, stack LGPL-3.0+ (`cores/no2usb/LICENSE.md`) | unknown (not cloned) |
| no2usb DFU **runtime** + `dfu_helper.v` | `smunaut__ice40-playground/projects/{riscv_usb,usb_audio,usb_amr}/` @ d2fa005; `icebreaker-fpga__icetwang/soc/ice-twang/` @ a4915ff; `osmocom__osmo-e1-hardware/gateware/icE1usb/` @ 85acea8 | iCE40 UP5K | gateware runtime only (detach + warmboot into the bootloader) | no2usb | app PIDs `1d50:6147`, `6175`, `615a`, `6145` | DFU runtime interface | `SB_WARMBOOT` to image 1 (DFU), image 2 (app) | LGPL-3.0+ / BSD (per file) | yosys + nextpnr-ice40 |
| OrangeCrab bootloader | not cloned (the OrangeCrab repos only use it) | OrangeCrab r0.2 (25F / 85F, CSFBGA285) | README says the bootloader creates a VexRiscv CPU (`orangecrab-fpga__orangecrab-examples/README.md:7` @ eefbafa); USB core unknown | unknown | `1209:5af0` (85F), `1209:5bf2` (25F) in `50-orangecrab.rules` | 0 = gateware | bootloader `0x0`, gateware `0x80000`, firmware `0x100000` (`litex/combine.py:9-12`) | unknown | unknown |
| Fomu **foboot** | not cloned (im-tomu/foboot), used by `im-tomu__fomu-workshop` @ af55dff | Fomu (iCE40 UP5K) | unknown (not cloned) | unknown | `1209:5bf0` (`docs/requirements/index.rst:33`) | 0 | `SB_WARMBOOT` image 0 = bootloader (`riscv-zig-blink/src/fomu/reboot.zig:9`) | unknown | unknown |
| Machdyne **tinydfu** | not cloned (machdyne/tinydfu-bootloader), described in `machdyne__zeitlos/docs/zboot.md` and `docs/dfu_upgrade.md` @ a7e7e85 | Lakritz (25F), Obst (12F), other Machdyne boards | gateware (top `tinydfu_lakritz.v`) | unknown | `16d0:116d` (all Machdyne boards, `docs/usb_cdc.md:204-207`) | 0 = user image | original: boot `0–0xFFFFF`, user `0x100000`; "256k" version: boot `0–0x3FFFF`, user `0x040000`; hand-off via PROGRAMN (site M8) after a 5 s timeout or DFU detach | unknown | unknown |
| pico-ice RP2040 firmware | `tinyvision-ai-inc__pico-ice-sdk/src/ice_usb.c` @ f3ddedc | pico-ice / pico2-ice (iCE40 UP5K) | **MCU** (RP2040, TinyUSB) | TinyUSB | `1209:b1c0` (`include/ice_usb.h:155-156`) | 0 = iCE40 flash, 1 = CRAM (`src/ice_usb.c:73-74`) | writes the iCE40's external flash or configures CRAM directly | MIT | pico-sdk / CMake |
| ESP32-S3 `dfu.py` | `emard__esp32ecp5/dfu.py` @ f6cea24 | ECP5 board with an ESP32-S3 running MicroPython ≥ 1.25 | **MCU** (ESP32-S3, programs ECP5 over JTAG via `ecp5.py`) | MicroPython `machine.USBDevice` (unverified) | `1d50:614b` (same ID as the ULX3S bootloader) | one alt; DfuSe-style addresses: `0` = SRAM, `0xF000000 + offset` = flash | any flash offset | MIT (pypi/LICENSE.txt, per catalogue) | none (Python script) |
| BlackIce / myStorm STM32 | `lawrie__blackicemxbook/STM32Programming/STM32Programming.md` @ ff5fdb3; STM32 DFU class in `hoglet67__ice40beeb/target/blackice/Middlewares/ST/.../Class/DFU/` @ e0fe38d | BlackIce II / Mx (iCE40) | **MCU** (STM32L4; `MCU = STM32L433xx` in `hoglet67__ice40beeb/target/blackice/Src/makefile:22`) | ST USB device library | `0483:df11` (STM32 DFU) | 0 | bitstream stored in STM32 internal flash at `0x0801F000` (`lawrie__hdmi_examples/Makefile:37` @ 30e2653) | ST license (unverified) | STM32 toolchain |

Not DFU, listed only so nobody looks for it here:
- `emard__tinyfpga-bootloader-ulx3s` @ 8e8ab80: a ULX3S build of phdussud's 60 MHz TinyFPGA
  bootloader fork (`README.md`). The ULX3S MANUAL says it is a vendor-specific USB device
  used with `tinyfpgasp` and is "less stable" than DFU
  (`emard__ulx3s/doc/MANUAL.md:427-431` @ 6a92cec).
- `ulixxe__usb_cdc` @ 6798bf4: USB CDC core. Its `examples/TinyFPGA-BX/hdl/bootloader/` is a
  CDC-based TinyFPGA bootloader, not DFU. The core itself contains no DFU class.

## ULX3S: the US2 DFU bootloader

### What it is
A bitstream stored at flash address 0. At power-on it:
- instantiates a PicoRV32 (`COMPRESSED_ISA=1`, no MUL/DIV/IRQ, `rtl/top-ulx3s.v:229-239`);
- runs 48 MHz from the 25 MHz oscillator (EHXPLLL, CLKOS output, `rtl/sysmgr.v`);
- drives the no2usb-style USB core on the **US2** pins `usb_fpga_bd_dp/dn` with pull-up
  `usb_fpga_pu_dp` (`rtl/top-ulx3s.v:101-103, 355-358`);
- reaches the flash through a QSPI master (`rtl/qspi_master_wb.v`, `rtl/qspi_phy_ecp5.v`,
  with SCK via `USRMCLK`, `rtl/top-ulx3s.v:428`);
- also bridges **US1** (FT231X) to the ESP32 (`rtl/esp32_passthru.v`), with I2C passthru.

The firmware (`fw/fw_dfu.c`, `fw/usb_dfu.c`) reads the buttons. If DFU is not requested,
it writes key `0xA5` to the misc block. This pulls the `user_programn` pin low
(`rtl/soc_had_misc.v:260`, LPF site `M4`: `data/top-ulx3s-v20.lpf:590-593`). The ECP5
then reconfigures from the BOOTADDR baked into the bootloader bitstream, which is
`0x200000` (`Makefile`: `ecppack --bootaddr $(USER_BITSTREAM_ADDR)`).

All paths in this section are `emard__had2019-playground/projects/bootloader/` @ 0723f2a
unless stated otherwise.

### USB identity
From `fw/usb_desc_dfu.c` and `fw/usb_str_dfu.txt`:

| Field | Value |
|---|---|
| VID:PID | `1d50:614b` (OpenMoko range), `bcdDevice` 0x0005 |
| Manufacturer / product | `FER-RADIONA-EMARD` / `ULX3S FPGA (DFU)` |
| Serial | the flash chip's unique ID, patched in at runtime (`fw_dfu.c: serial_no_init`) |
| DFU functional descriptor | `bmAttributes=0x0d`, `wTransferSize=4096`, `bcdDFUVersion=0x0101`, `wDetachTimeOut=1000` |
| Extras | MS OS 2.0 descriptor with `WINUSB` compatible ID, so Windows binds WinUSB without a driver install |

### Alt settings
`dfu_zones[]` in `fw/usb_dfu.c:164-172`:

| Alt | Flash range | Name string | Notes |
|---|---|---|---|
| 0 | `0x200000–0xFFFFFF` | User Bitstream | normal target |
| 1 | `0x340000–0x35FFFF` | Saxonsoc fw_jump | |
| 2 | `0x360000–0x3FFFFF` | Saxonsoc u-boot | |
| 3 | `0x400000–0xFFFFFF` | User Data | |
| 4 | `0x800000–0xFFFFFF` | User Data | |
| 5 | `0x000000–0x1FFFFF` | Bootloader Bitstream | hidden unless the upgrade button is held: firmware trims the last 18 bytes (interface + DFU descriptor) off `wTotalLength` (`fw/fw_dfu.c`) |
| (6) | `0x000000–0x0000FF` on "cart" flash | RTC | present in `dfu_zones[]` and strings, but `usb_desc_dfu.c` only declares six interfaces (alts 0–5), so unreachable as built |

### Buttons and modes (ULX3S)
`rtl/top-ulx3s.v:301-308` remaps the debounced buttons into the badge's bit layout. The
firmware tests `BTN_SELECT` (bit 6) = stay in DFU and `BTN_START` (bit 7) = bootloader
writable (`fw/misc.h:32-33`, `fw/fw_dfu.c`):

| Held while plugging US2 | Result |
|---|---|
| nothing | jump to the user bitstream at `0x200000` (LEDs blink if none is valid, as the bootloader keeps restarting) |
| BTN1, or DIP SW1 = ON | stay in DFU, alts 0–4, bootloader flash region write-protected. LEDs D0–D2 on, D3–D7 off |
| BTN1 + BTN2 | stay in DFU and expose alt 5 (bootloader region writable) |
| BTN2 alone | removes the flash write protection but does not stay in DFU |

The firmware also stays in DFU if the two PSRAMs hold the magic `0x21554644` ("DFU!").
That is a badge feature, and the ULX3S has no PSRAM, so its effect there is unknown.
For a board without buttons, the README suggests hard-wiring
`assign btn_remap_i = ~8'b1100000;` (`README.md`).

To leave DFU and start the user bitstream: `dfu-util -a 0 -e`. The MANUAL recommends
soldering diode **D28** so that BTN0 pulls PROGRAMN and cycles to the next multiboot image
(`emard__ulx3s/doc/MANUAL.md:436-444` @ 6a92cec).

### Install the bootloader (first time, needs US1/JTAG)
Prebuilt multiboot images are in `emard__ulx3s-bin/fpga/dfu/<size>-<rev>/multiboot.img.gz`
@ 2a40f50, for `12f-v20`, `12f-v314`, `12f-v317`, `25f-v20`, `45f-v20`, `85f-v20`, `85f-v317`,
`m85f-v20` (ECP5-5G) and `ulx4m-um85f-v002`. Each folder also holds a `passthru<idcode>.bit.gz`.
These images are present in the local clone but were not tested. From
`emard__ulx3s-bin/fpga/dfu/README.md`:

```sh
fujprog -j flash multiboot.img
# or
openFPGALoader -b ulx3s --unprotect-flash --file-type bin -f multiboot.img.gz
```

The multiboot image is built by `ecpmulti` (`Makefile`, target `$(BUILD_TMP)/multiboot.img`):
- the bootloader at `0x000000`;
- a passthru bitstream at `0x200000` as a placeholder user image;
- `--flashsize 128` (Mbit).

### Load user bitstreams
Enter DFU mode (BTN1 or SW1 held while plugging US2), then (`README.md`,
`emard__ulx3s-bin/fpga/dfu/README.md`, `emard__ulx3s/doc/MANUAL.md:421-425`):

```sh
dfu-util -a 0 -D blink.bit           # write alt 0 (flash 0x200000)
dfu-util -a 0 -e                     # leave DFU, boot the user bitstream
dfu-util -a 0 -R -D blink.bit        # one-liner, "sometimes" works
zcat blink.bit.gz | dfu-util -a 0 -D -
openFPGALoader -b ulx3s_dfu blink.bit.gz
openFPGALoader --dfu --vid 0x1d50 --pid 0x614b --altsetting 0 blink.bit
dfu-util -l                          # list alt settings
```

openFPGALoader defines `ulx3s_dfu` and `ulx4m_dfu` as `DFU_BOARD(..., 0x1d50, 0x614b, 0)`
(`trabucayre__openfpgaloader/src/board.hpp:275,277` @ 676e53e). They are flash-only
(`doc/boards.yml:990-1002`: `Memory: NA`, `Flash: OK`). See
[trabucayre__openfpgaloader](projects/trabucayre__openfpgaloader.md).

udev rule from the README (Linux, non-root):

```
ATTRS{idVendor}=="1d50", ATTRS{idProduct}=="614b", GROUP="dialout", MODE="666"
```

A user bitstream needs nothing special: plain `ecppack` output works, since it is written at
`0x200000` and the bootloader's BOOTADDR points there. A user design that wants to go back
to the bootloader must pull PROGRAMN (`M4`). Its own BOOTADDR is 0 by default, so the
reload lands on the bootloader. Keep `SYSCONFIG MASTER_SPI_PORT=ENABLE` and do not use
`USRMCLK` if the ESP32 write-protect tool must reach the flash over JTAG (`README.md`,
"Using ecp5wp.py").

### Build from source
`Makefile` variables: `MODEL ?= ulx3s|ulx4m`, `BOARD ?= $(MODEL)-v20|-v314|-v317|-v002`,
`DEVICE = 12k` (override on the command line), `USER_BITSTREAM_ADDR := 0x200000`. Targets:

| Target | What it does |
|---|---|
| `make` / `synth` | yosys `synth_ecp5` → nextpnr-ecp5 → `ecpbram` inserts `fw/fw_dfu.hex` into BRAM → `ecppack --spimode qspi --freq 38.8 --bootaddr 0x200000 --compress` (`build/project-rules.mk`, project `Makefile`) |
| `multi` | `multiboot.img.gz` via `ecpmulti` + `gzip4k.py` |
| `flash` / `flash_ofl` | write `multiboot.img` with fujprog / openFPGALoader over US1 |
| `flash_dfu` | self-upgrade over DFU: first 2 MB to alt 5, passthru to alt 0 (hold BTN1+BTN2) |
| `pass_dfu` | write the passthru bitstream to alt 0 |

The firmware needs `riscv-none-embed-gcc` with `-march=rv32iac` (`fw/Makefile`). Two
prebuilt firmware hex files are committed: `fw/fw_dfu.hex-0x180000` (badge layout) and
`fw/fw_dfu.hex-0x200000` (ULX3S layout). The commented `cp` line in `Makefile` suggests
they can replace a firmware build. The user offset appears in three places that **must
agree**:
- `USER_BITSTREAM_ADDR` in `Makefile`;
- `dfu_zones[0]` in `fw/usb_dfu.c`;
- the `ecpmulti --address`.

For ULX4M with an `um-85k` (ECP5-5G IDCODE), `ecpmulti` needs
`--input-idcode 0x01113043 --output-idcode 0x01113043` (comment in `Makefile`). Hazard3-Doom's
Makefile automates this. Not built during this review.

### Flash write protection
The firmware sets the flash's non-OTP block protection over the first 2 MB. It does this
unless BTN2 is held (`flash_write_protect_bootloader()` in `fw/fw_dfu.c`). The README says:
- this works for Winbond W25Q128 and ISSI IS25LP128;
- the 4 MB IS25LP032 "can't protect";
- `esp32ecp5`'s `ecp5wp.py` can set it from the ESP32, including the one-time ISSI TBS bit.

openFPGALoader "will silently remove non-OTP write protection". This is why the
ulx3s-bin install command uses `--unprotect-flash`.

### ULX4M
Two ULX4M tops exist:
- `emard__had2019-playground/.../rtl/top-ulx4m.v`: button bit 7 ← `btn[2]`, bit 6 ← `btn[1]`,
  SW1 line commented out.
- `ulx3s__hazard3-doom/bootloader/rtl/top-ulx4m.v` @ 4262159: remapped and **validated on
  ULX4M-LD v0.0.3 / LFE5UM-85F**. PCB BTN3 (`btn[2]`) = stay in DFU, PCB BTN2 (`btn[1]`) =
  upgrade. It adds `EMERGENCY_RESTORE1/2` defines that force DFU (and alt 5) for JTAG-loaded
  SRAM recovery images.

`bootloader/README_ULX4M_BOOTLOADER.md` is the most complete procedure in the collection. It
covers:
- the USB pins F4/E3/F5;
- an SRAM test image (`ecppack` without `--bootaddr`);
- backing up alt 5 with `dfu-util -a 5 -U`;
- writing exactly 2 MiB to alt 5 from an SRAM-running bootloader;
- a byte-for-byte readback before power-cycling.

The ULX4M port of Hazard3 gives a different entry method, "move either ULX4M SW1 slider to
ON" (`ulx3s__hazard3/example_soc/synth/ULX4M_PORT.md:21-24` @ 3c0aca0). Which applies depends
on the bootloader build and board variant, so this is unresolved (see open questions).

### ESP32-S3 alternative (MCU DFU)
`emard__esp32ecp5/dfu.py` @ f6cea24 makes an ESP32-S3 running MicroPython ≥ 1.25 re-enumerate
as DFU `1d50:614b`, with DfuSe-style addressing (`README.md:680-721`):

```sh
dfu-util -s 0:leave -D bitstream.bit              # FPGA SRAM
dfu-util -s 0xF200000:leave -D bitstream.bit      # flash @ 0x200000 (user)
dfu-util -s 0xF200000:0xE00000:leave -U read.bit  # read back
```

The ULX3S carries an ESP32 (WROOM), not an S3. Which board this targets is unknown from the
source.

## Other boards

### OrangeCrab (ECP5 25F/85F)
The bootloader is not in the collection. Every OrangeCrab project packs `ecppack --compress
--freq 38.8`, then adds a DFU suffix and loads alt 0
(`orangecrab-fpga__orangecrab-examples/verilog/blink/Makefile:30-52` @ eefbafa):

```sh
dfu-suffix -v 1209 -p 5af0 -a blink.dfu
dfu-util --alt 0 -D blink.dfu
```

A user design returns to the bootloader by driving `rst_n` (pin V17, wired to PROGRAMN) low
from the button (`verilog/blink_reset/blink_reset.v:32-38`, `verilog/orangecrab_r0.2.1.pcf:255`).
RISC-V firmware for the bootloader's own VexRiscv goes to a separate flash region: the linker
has `spiflash ORIGIN = 0x20000000 + 0x80000` (`riscv/blink/sections.ld`), and
`riscv/blink/Makefile` uses PIDs `5bf0` and `5af0`.

`litex/combine.py` places the gateware at `0x80000` and CircuitPython at `0x100000`, but
suffixes with PID `5bf0`, unlike the Verilog examples. This inconsistency is recorded, not
resolved.

### Fomu (iCE40 UP5K)
foboot, `1209:5bf0`, version 2.0.3 required by the workshop
(`im-tomu__fomu-workshop/docs/requirements/index.rst:1-33` @ af55dff). The workshop's HDL flow
suffixes with a different PID and loads with plain `dfu-util -D`
(`hdl/PnR_Prog.mk:17-24`):

```sh
dfu-suffix -v 1209 -p 70b1 -a blink.dfu
dfu-util -D blink.dfu
```

The same `70b1` suffix appears in `chrismoos__m6502/targets/fomu/PnR_Prog.mk` @ 4471944,
`stnolting__neorv32-setups/osflow/boards/Fomu.mk` @ 57f86d5,
`brunolevy__learn-fpga/Basic/FOMU/FOMU_VGA/makeit.sh` @ 5c08c87 and
`ulixxe__usb_cdc/examples/Fomu/OSS_CAD_Suite/Makefile` @ 6798bf4. User code reboots to the
bootloader with `SB_WARMBOOT` image 0 (`riscv-zig-blink/src/fomu/reboot.zig`).

### iCEBreaker-bitsy, reDIP-SID, icE1usb (no2bootloader, iCE40 UP5K)
- **iCEBreaker-bitsy**: `dfu-util -d 1d50:6146 -a 0 -D top.bin -R`
  (`icebreaker-fpga__icebreaker-verilog-examples/main.mk:40-48` @ 8d0892b). `dfu-util -l`
  shows alt 0 "iCE40 bitstream", alt 1 "RISC-V firmware", and a runtime device `1d50:6147`
  (`icebitsy/README.md`). Examples include `icebitsy/common/dfu_helper.v`: a long button press
  reboots into DFU.
- **reDIP-SID**: `dfu-util -d 1d50:6159,:6156 -a 0 -D redip_sid.bin -R`
  (`daglem__redip-sid/gateware/Makefile:68` @ 5660867). The same command is in
  `bit-hack__icesid/reDIP-SID/Makefile.mk:43` @ b126c46. The bundled `muacm.v`
  (no2muacm USB-CDC) has a patchable `dfu_disable` field (`gateware/muacm.v:20462`), which
  suggests μACM can expose a DFU runtime interface (unverified).
- **icE1usb**: bootloader `1d50:6144`, application `1d50:6145`. Detach with
  `dfu-util -d 1d50:6145 -e`, gateware on alt 0, picoRV32 firmware on alt 1. The recessed
  button forces DFU at power-up
  (`osmocom__osmo-e1-hardware/doc/manuals/chapters/icE1usb/firmware.adoc:11-70` @ 85acea8).
- `emeb__up5k_osc/gateware/icestorm/Makefile:69-70` @ a24453f also targets `1d50:6146`.

The **runtime side** is in the collection: `dfu_helper.v`
(`smunaut__ice40-playground/projects/riscv_usb/rtl/dfu_helper.v` @ d2fa005). It debounces a
button:
- a short press resets the app;
- a long press drives `SB_WARMBOOT` with `S1:S0 = 01` (DFU image);
- in bootloader mode (`DFU_MODE=1`) any press boots image `10` (app).

Firmware answers DFU_DETACH through `no2usb/fw/v0/src/usb_dfu_rt.c` and reboots by writing
`(1<<2)|(1<<0)` to `0x80000000` (`projects/riscv_usb/fw/fw_app.c:61-75`).

### pico-ice / pico2-ice (RP2040/RP2350 + iCE40 UP5K)
The DFU is done by the **RP2040** with TinyUSB (`tinyvision-ai-inc__pico-ice-sdk/src/ice_usb.c`
@ f3ddedc). It enumerates as `1209:b1c0`, with alt 0 "iCE40 DFU (Flash)" and alt 1 "iCE40 DFU
(CRAM)". The alt numbers were swapped in v1.5.0 for APIO/IceStudio (`CHANGELOG.md:8-12`).

```sh
dfu-util -d 1209:b1c0 -a 0 -D gateware.bin -R     # examples/ice_makefile_iverilog_counter/Makefile
```

### BlackIce II / Mx (STM32 + iCE40)
DFU is the **STM32** ROM/firmware DFU. It is used to reflash the myStorm firmware
(`dfu-util -s 0x08000000:leave -a 0 -D mystorm.raw -t 1024`,
`lawrie__blackicemxbook/STM32Programming/STM32Programming.md:19-25` @ ff5fdb3). It is also
used to store an iCE40 bitstream in STM32 flash:
`dfu-util -d 0483:df11 --alt 0 --dfuse-address 0x0801F000 -D chip.bin`
(`lawrie__hdmi_examples/Makefile:37` @ 30e2653, `wuxx__icesugar/src/advanced/icicle/boards/blackice-ii.mk:10` @ 1ebe71b).

### Machdyne Lakritz / Obst (ECP5)
tinydfu, `16d0:116d`. Zeitlos documents a bootloader upgrade that shrinks the boot
partition to 256 KB so the user partition starts at `0x040000`. It gives this warning:
"`dfu-util` uses one [offset], `ecppack` bakes in the other, and a mismatch produces a board
that accepts a write and then does not boot" (`machdyne__zeitlos/docs/zboot.md:80-124`,
`docs/dfu_upgrade.md` @ a7e7e85). Load: `sudo dfu-util -a 0 -D zeitlos-lakritz_gpio-dfu.bin`
(`README.md:197`). openFPGALoader has `LD-SCHOKO-DFU` and `LD-KONFEKT-DFU` = `16d0:116d`
(`src/board.hpp:210,212`).

## Projects that only use DFU to load

These projects run `dfu-util` or `openFPGALoader --dfu` on their own bitstream and contain no
DFU implementation.

| Repo @ commit | Board | Command (file) |
|---|---|---|
| `emard__ulx3s-misc` @ d0c6f15 (and copies of the same `scripts/trellis_main_ghdl.mk` in `goran-mahovlic__odysseus_sprites` @ ee59a0f, `emard__ulx3s-emi` @ 8c93799, `tarik-hamedovic__sdr-hls` @ 334f707, `advikbahadur__ulx3s-superresolution-cnn` @ 7979af3; `stuij__odyssey` @ e74caa8 `scripts/diamond_main.mk:242`; `emard__galaksija` / `emard__ulx3s_galaksija` @ ddcbf3a `proj/lattice/scripts/trellis_main.mk:201`) | ULX3S | `make flash_dfu` → `dfu-util -a 0 -D x.bit; dfu-util -a 0 -e` (`scripts/trellis_main_ghdl.mk:199-202`) |
| `lawrie__ulx4m_examples` @ 415ee53 | ULX4M | `make dfu` → `dfu-util -a 0 -D toplevel.bit -R` (`ulx4m.mk:14-15`). "Hold down btn 1 when powering up" (`README.md:15`) |
| `lawrie__ulx4m_amaranth_examples` @ 89bff9e | ULX4M | Amaranth platform `toolchain_program` → `dfu-util -a 0 -D <bit> -R` (`*/ulx4m.py:102-116`) |
| `lawrie__ulx3s_zx81` @ 8219f3b, `lawrie__jupiter_ace` @ ace1bce, `danodus__ulx3s_sms` @ 13c2361, `lawrie__apple-one` @ 40412e9 | ULX4M | `dfu-util -a 0 -D toplevel.bit -R` (`ulx4m/ulx4m.mk:14-15`; apple-one `boards/ulx4m/yosys/Makefile:64-65`) |
| `ulx3s__hazard3` @ 3c0aca0 | ULX4M-LS/LD, OrangeCrab 25F | `dfu-util -a 0 -D $(CHIPNAME).bit -R` (`example_soc/synth/ULX4M_LD_85F.mk:58-60`); `openFPGALoader --dfu --vid 0x1d50 --pid 0x614b --altsetting 0` (`ULX4M_PORT.md:41`); OrangeCrab `dfu-util -d 1209:5af0` (`orangecrab-25f.mk:23`, also in `wren6991__hazard3` @ 8af9929) |
| `joshajohnson__ecp5-mini-projects` @ 4e86228 | ECP5 Mini | `dfu-util -d 1d50:614b -a 0 -R -D x.bit` (`verilog/common.mk:46`). `verilog/common/dfu_reset.v`: three button presses pull PROGRAMN |
| `spritetm__hadbadge2019_fpgasoc` @ 6e706d5 | HAD2019 badge | `make dfu_flash` → `dfu-util -d 1d50:614a,1d50:614b -a 0 -R -D soc.bit` (`soc/Makefile:204-212`) |
| `litex-hub__linux-on-litex-vexriscv` @ 05fc5e4 | HAD2019 badge | `dfu-util --alt 2 --download <bit> --reset` (`boards.py`, class `HADBadge`) |
| `orangecrab-fpga__orangecrab-examples` @ eefbafa, `mangelajo__orangecrab-usb` @ c4a8293, `fdarling__orangecrab-usb-cdc-demo` @ 36a88f0, `tallenintegsys__hdmi-orangecrab` @ 5943656, `hsa-ees__piconut` @ 826460d, `sylefeb__silice` @ 620487d | OrangeCrab | `dfu-suffix -v 1209 -p 5af0 -a x.dfu; dfu-util [-a 0] -D x.dfu` (e.g. `mangelajo__orangecrab-usb/common.mk:36,71`; `silice frameworks/boards/orangecrab/orangecrab.sh:44-46`; `piconut boards/piconut-boards.mk:228-239`) |
| `ultraembedded__orangecrab` @ 685d601 | OrangeCrab | prebuilt `ddr_test/bitstreams/ddr_test_r0_2.dfu` only (per catalogue), no Makefile |
| `fusesoc__blinky` @ 496eae5 | OrangeCrab, Fomu | post-run hook prints `dfu-util -d 1209:5af0 -D …` / `dfu-util -e -d 1209:5bf0 -D …` (`sw/proginfo.py:18-22`) |
| `im-tomu__fomu-workshop`, `chrismoos__m6502`, `stnolting__neorv32-setups`, `brunolevy__learn-fpga`, `ulixxe__usb_cdc` | Fomu | `dfu-suffix -v 1209 -p 70b1` + `dfu-util -D` (see Fomu above) |
| `icebreaker-fpga__icebreaker-verilog-examples`, `icebreaker-fpga__icetwang`, `emeb__up5k_osc` | iCEBreaker-bitsy | `dfu-util -d 1d50:6146 -a 0 -D x.bin -R` |
| `daglem__redip-sid`, `bit-hack__icesid` | reDIP-SID | `dfu-util -d 1d50:6159,:6156 -a 0 -D x.bin -R` |
| `tinyvision-ai-inc__pico-ice-sdk` | pico-ice | `dfu-util -d 1209:b1c0 -a 0 -D gateware.bin -R` |
| `lawrie__hdmi_examples`, `wuxx__icesugar` (icicle, BlackIce II), `hoglet67__ice40beeb` @ e0fe38d, `hoglet67__ice40atom` @ 28e4363 | BlackIce (STM32) | `dfu-util -d 0483:df11 --alt 0 --dfuse-address 0x0801F000 -D chip.bin` |

## Reuse guidance

**New ECP5 design (ULX3S-like, full-speed USB on two FPGA pins):** reuse the
`emard__had2019-playground` bootloader. Take the Hazard3-Doom copy if you want a
self-contained tree with vendored build rules and a validated recovery procedure. It is the
only ECP5 DFU bootloader in the collection with full source. What to change:
1. **Top and LPF**: the USB D+/D−/pull-up pins, the 25 MHz → 48 MHz PLL (`sysmgr.v` if your
   oscillator differs), the LEDs, the button remap (`btn_remap_i`), and the pin wired back to
   PROGRAMN. Without a PROGRAMN loop-back the bootloader cannot hand over.
2. **Offsets**: `USER_BITSTREAM_ADDR`, `dfu_zones[]` and the `ecpmulti --address` must agree.
   The bootloader bitstream must fit below the user offset (2 MB reserved on ULX3S, while
   tinydfu fits in 256 KB).
3. **USB identity**: `1d50:614b` and the strings are allocated to ULX3S/ULX4M. openFPGALoader
   and udev rules key on them. A different board should get its own PID.
4. **Flash protection**: `flash_write_protect_bootloader()` in `fw/spi.c` is
   vendor-specific (Winbond/ISSI 16 MB). Check it for your flash chip, or disable it.
5. **Firmware toolchain**: `riscv-none-embed-*` names. Hazard3-Doom's README shows a symlink
   shim for `riscv32-unknown-elf-*`.
6. **ECP5-5G / IDCODE**: pass `--input-idcode/--output-idcode` to `ecpmulti` when mixing
   LFE5U and LFE5UM images.

The USB core in that tree is an **early snapshot of no2usb**. It is ECP5-capable through a
`TRELLIS_IO` branch in `usb_phy.v` and inferred RAM when `USB_ARCH_ICE40` is undefined
(`cores/usb/rtl/usb_ep_buf.v:50`, `usb_ep_status.v:102`). The current no2usb README still
says the ECP5 tweaks "haven't been added here yet"
(`smunaut__ice40-playground/cores/no2usb/README.md` @ d359102). So for ECP5, take the
had2019 copy, not upstream no2usb, unless you port the IO/RAM primitives yourself.

**New iCE40 UP5K design:** use no2bootloader. It is not in the collection, so clone
`no2fpga/no2bootloader` before relying on its layout. In your application:
- instantiate `dfu_helper.v` (long-press → `SB_WARMBOOT` to the DFU image);
- if the app has USB, add the DFU runtime interface from `no2usb/fw/v0/src/usb_dfu_rt.c`, so
  `dfu-util -e` / `-R` can detach without a button.

If the board has an RP2040, the pico-ice-sdk's TinyUSB DFU (alt 0 flash, alt 1 CRAM) needs no
FPGA-side support at all.

**Design that only loads through someone else's bootloader:** use plain `ecppack` / `icepack`
output. OrangeCrab and Fomu flows add a `dfu-suffix`, while ULX3S/ULX4M flows write the raw
`.bit`: dfu-util 0.9 warns "Invalid DFU suffix" but proceeds
(`ulx3s__hazard3-doom/bootloader/README_ULX4M_BOOTLOADER.md` §15). To return to the
bootloader from a running design:
- ECP5: pull PROGRAMN low;
- iCE40: fire `SB_WARMBOOT`.

## Open questions

- HAD2019 badge original (smunaut/had2019-playground), no2bootloader, OrangeCrab bootloader,
  foboot and tinydfu are **not cloned**. Their USB cores, licenses and exact flash layouts are
  unknown here. They are candidates for `clone.sh`.
- ULX4M DFU entry: the Hazard3-Doom README says PCB BTN3, while `ulx3s__hazard3/.../ULX4M_PORT.md`
  says the SW1 slider. This is probably different bootloader builds or board variants (LD vs
  LS); unverified.
- Which board `emard__esp32ecp5/dfu.py` targets (an ESP32-S3 on an ECP5 board, but reusing the
  ULX3S bootloader's `1d50:614b`) is unknown.
- `1d50:614a` (accepted next to `614b` in badge and bootloader Makefiles) is presumably the
  badge's own PID. Not verified, since the badge source is not cloned.
- OrangeCrab examples use PID `5af0` (85F) in Verilog flows but `5bf0` in `litex/combine.py`
  and `riscv/blink`, and udev lists `5bf2` for 25F. Which PID each bootloader revision uses is
  unknown.
- The RTC alt (zone 6) in the ULX3S firmware is unreachable with the committed descriptor.
  Whether any build exposes it is unknown.
- None of the bootloaders were built or run during this review.
