# pi5-mg90s-tools

树莓派 Pi5 的舵机 MG90S 的使用

## 示例

示例脚本位于 `examples/` 目录。运行前需安装 `gpiozero` 及 `lgpio`:

```bash
sudo apt install python3-gpiozero python3-lgpio
```

执行：

```bash
python3 examples/main.py --pin 18
```

`--pin` 指定舵机连接的 BCM 引脚，默认为 18。脚本会循环将舵机从最小角度移动到最大角度。

## 许可

本项目采用 MIT 许可协议。
