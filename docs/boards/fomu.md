---
title: "Fomu"
parent: "iCE40 UP5K boards"
grand_parent: "Boards"
nav_order: 4
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Fomu

UP5K board that fits inside a USB port; foboot DFU bootloader.

| | |
|---|---|
| Board | Fomu (in-USB-port board) |
| FPGA | iCE40 UP5K, UWG30 |
| Evidence | catalogue rows (im-tomu__fomu-workshop) |
| Clock | unknown |
| Catalogued repos | 7 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`pcf/fomu-hacker.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-hacker.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-pvt.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-pvt.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-evt3.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-evt3.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-evt2.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-evt2.pcf) | im-tomu__fomu-workshop |
| [`gateware/ice40/data/top-fomu-hacker.pcf`](https://github.com/no2fpga/no2bootloader/blob/37dda02fba084f85f6da31ee228d3bbabbb91add/gateware/ice40/data/top-fomu-hacker.pcf) | no2fpga__no2bootloader |
| [`gateware/ice40/data/top-fomu-pvt1.pcf`](https://github.com/no2fpga/no2bootloader/blob/37dda02fba084f85f6da31ee228d3bbabbb91add/gateware/ice40/data/top-fomu-pvt1.pcf) | no2fpga__no2bootloader |
| [`gateware/ice40-stub/data/top-fomu-hacker.pcf`](https://github.com/no2fpga/no2bootloader/blob/37dda02fba084f85f6da31ee228d3bbabbb91add/gateware/ice40-stub/data/top-fomu-hacker.pcf) | no2fpga__no2bootloader |
| [`gateware/ice40-stub/data/top-fomu-pvt1.pcf`](https://github.com/no2fpga/no2bootloader/blob/37dda02fba084f85f6da31ee228d3bbabbb91add/gateware/ice40-stub/data/top-fomu-pvt1.pcf) | no2fpga__no2bootloader |
| [`boards/Tomu_Fomu/pins.pcf`](https://github.com/tinyfpga/TinyFPGA-Bootloader/blob/97f6353540bf7c0d27f5612f202b48f41da75299/boards/Tomu_Fomu/pins.pcf) | tinyfpga__tinyfpga-bootloader |
| [`examples/Fomu/OSS_CAD_Suite/pcf/fomu-hacker.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/Fomu/OSS_CAD_Suite/pcf/fomu-hacker.pcf) | ulixxe__usb_cdc |
| [`examples/Fomu/OSS_CAD_Suite/pcf/fomu-pvt.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/Fomu/OSS_CAD_Suite/pcf/fomu-pvt.pcf) | ulixxe__usb_cdc |
| [`examples/Fomu/OSS_CAD_Suite/pcf/fomu-evt3.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/Fomu/OSS_CAD_Suite/pcf/fomu-evt3.pcf) | ulixxe__usb_cdc |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| Fomu foboot DFU bootloader (LiteX/VexRiscv + ValentyUSB eptri) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | im-tomu__foboot |
| TinyFPGA USB Bootloader (USB-serial-to-SPI-flash bridge) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | tinyfpga__tinyfpga-bootloader |
| no2bootloader (Nitro) iCE40 UP5K DFU bootloader | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | no2fpga__no2bootloader |
| no2usb DFU runtime + dfu_helper.v (iCE40) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | smunaut__ice40-playground |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| LAYR_AUDIO SID6581 sound chip core | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | thorkn__layr_audio |
| SPI master (Bus Pirate NextGen Ultra) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | dangerousprototypes__buspirateultrahdl |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |
| no2usb-derived ECP5 USB FS device core (had2019 bootloader) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | emard__had2019-playground |
| ulixxe USB CDC-ACM device core | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | ulixxe__usb_cdc |

## Projects targeting this board

- [google__cfu-playground](https://github.com/google/CFU-Playground): CFU-Playground: framework for building/benchmarking custom CFU
- [im-tomu__foboot](https://github.com/im-tomu/foboot): Foboot: the Fomu iCE40 UP5K failsafe USB DFU bootloader, LiteX/Migen SoC
- [im-tomu__fomu-workshop](https://github.com/im-tomu/fomu-workshop): Fomu: a multi-language FPGA workshop
- [litex-hub__litex-boards](https://github.com/litex-hub/litex-boards): LiteX board-support collection: Python platform + target definitions
- [no2fpga__no2bootloader](https://github.com/no2fpga/no2bootloader): Nitro Bootloader: iCE40 UP5K DFU bootloader
- [tinyfpga__tinyfpga-bootloader](https://github.com/tinyfpga/TinyFPGA-Bootloader): TinyFPGA USB Bootloader: USB virtual-serial-to-SPI-flash-bridge gateware bootloader;
- [ulixxe__usb_cdc](https://github.com/ulixxe/usb_cdc): Fomu / TinyFPGA-BX: USB_CDC, a from-scratch Full-Speed ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/ulixxe__usb_cdc.md))
{% endraw %}
