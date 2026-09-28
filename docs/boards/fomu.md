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
| Catalogued repos | 2 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`pcf/fomu-hacker.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-hacker.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-pvt.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-pvt.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-evt3.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-evt3.pcf) | im-tomu__fomu-workshop |
| [`pcf/fomu-evt2.pcf`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/pcf/fomu-evt2.pcf) | im-tomu__fomu-workshop |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/bootloader/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/bootloader/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/demo/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/demo/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback_2ch/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback_2ch/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback_7ch/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/loopback_7ch/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/OSS_CAD_Suite/input/soc/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/OSS_CAD_Suite/input/soc/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/iCEcube2/bootloader/constraints/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/iCEcube2/bootloader/constraints/pins.pcf) | ulixxe__usb_cdc |
| [`examples/TinyFPGA-BX/iCEcube2/demo_allverilog/constraints/pins.pcf`](https://github.com/ulixxe/usb_cdc/blob/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/examples/TinyFPGA-BX/iCEcube2/demo_allverilog/constraints/pins.pcf) | ulixxe__usb_cdc |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/ulx3s-klod/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |
| ulixxe USB CDC-ACM device core | [usb-device](https://github.com/kelu124/ulx3s-klod/blob/main/functions/usb-device.md) | ulixxe__usb_cdc |

## Projects targeting this board

- [im-tomu__fomu-workshop](https://github.com/im-tomu/fomu-workshop): Fomu: a multi-language FPGA workshop
- [ulixxe__usb_cdc](https://github.com/ulixxe/usb_cdc): Fomu / TinyFPGA-BX: USB_CDC, a from-scratch Full-Speed ([review](https://github.com/kelu124/ulx3s-klod/blob/main/projects/ulixxe__usb_cdc.md))
{% endraw %}
