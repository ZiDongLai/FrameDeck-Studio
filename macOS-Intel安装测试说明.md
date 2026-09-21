# FrameDeck Studio macOS Intel版安装与测试说明

适用安装包：`FrameDeck-Studio-v12.0.0-macOS-x86_64.dmg`

适用设备：搭载 Intel Core i5、i7 或 i9 处理器的 Mac。Apple M1、M2、M3、M4 等设备应使用 arm64 版本。

> 当前测试包采用免费 ad-hoc 签名，未完成 Apple Developer ID 签名和公证。首次启动时出现安全提示属于预期情况，不需要关闭系统全局安全功能。

## 一、确认电脑架构

打开“终端”，执行：

```bash
uname -m
```

Intel Mac 应显示：

```text
x86_64
```

如果显示 `arm64`，请不要安装本文件对应的 Intel 版本，应下载 arm64 版本。

## 二、下载测试包

1. 打开本仓库的 **Actions** 页面。
2. 选择 **macOS Intel x86_64 Test Build**。
3. 打开最新一次成功的运行记录。
4. 在页面底部 **Artifacts** 区域下载：
   `FrameDeck-Studio-v12.0.0-macOS-x86_64-unsigned-test`
5. 解压下载的 Artifact，里面包含 DMG、ZIP 和 SHA-256 校验文件。
6. 优先测试 DMG；ZIP 仅作为备用分发格式。

## 三、校验安装包

假设文件位于“下载”目录，执行：

```bash
cd ~/Downloads
shasum -a 256 "FrameDeck-Studio-v12.0.0-macOS-x86_64.dmg"
cat "SHA256SUMS-macOS-x86_64.txt"
```

DMG 对应的两段 SHA-256 必须一致。

检查磁盘映像完整性：

```bash
hdiutil verify "FrameDeck-Studio-v12.0.0-macOS-x86_64.dmg"
```

结果应包含 `VALID`。

## 四、安装

1. 双击打开 DMG。
2. 将 **FrameDeck Studio.app** 拖入 **Applications（应用程序）**。
3. 弹出磁盘映像。
4. 从“应用程序”目录启动 FrameDeck Studio。

## 五、首次启动被阻止时

如果系统提示无法验证开发者或阻止应用运行：

1. 关闭提示窗口。
2. 打开“系统设置”。
3. 进入“隐私与安全性”。
4. 向下找到 FrameDeck Studio 被阻止的提示。
5. 点击“仍要打开”。
6. 输入当前 Mac 的登录密码或使用 Touch ID。
7. 再次确认“打开”。

只需要针对当前版本首次执行一次。不要运行 `sudo spctl --master-disable`，也不要全局关闭 Gatekeeper。

## 六、确认程序确实是Intel版本

执行：

```bash
file "/Applications/FrameDeck Studio.app/Contents/MacOS/FrameDeck Studio"
```

输出中必须包含：

```text
x86_64
```

进一步检查应用信息：

```bash
/usr/libexec/PlistBuddy -c "Print :CFBundleIdentifier" "/Applications/FrameDeck Studio.app/Contents/Info.plist"

codesign -dv --verbose=4 "/Applications/FrameDeck Studio.app" 2>&1 | grep -E "Identifier|Format|Signature|TeamIdentifier"
```

预期 Bundle ID：

```text
com.zidonglai.framedeckstudio
```

当前未公证测试版显示 `Signature=adhoc` 或没有开发者团队信息属于预期情况。

## 七、功能测试

请至少验证以下内容：

- 软件能够正常启动、退出和再次启动。
- 中文和英文界面能够切换。
- 添加 JPG、PNG、HEIC/HEIF 等常用图片。
- 创建多页排版并切换页面。
- 调整图片缩放、位置、裁切及页面布局。
- 添加、修改和删除标题。
- 保存工程，关闭软件后重新打开工程。
- 导入 PPT。
- 导出 PPT，并在 PowerPoint 或 Keynote 中打开。
- 检查导出的图片、标题、页码和排版位置。
- 连续操作至少 15 分钟，确认没有闪退或明显卡顿。

## 八、反馈格式

测试后请记录：

```text
电脑型号：
macOS版本：
处理器：
内存：
安装包SHA-256：
是否成功安装：
是否需要“仍要打开”：
是否正常启动：
图片导入：
工程保存/打开：
PPT导入：
PPT导出：
中文/英文切换：
发现的问题：
```

如发生闪退，请立即执行以下命令并保存结果：

```bash
log show --last 10m --predicate 'process == "FrameDeck Studio"' --style compact > ~/Desktop/FrameDeck-Intel-log.txt
```

## 九、卸载

退出软件后，将“应用程序”中的 **FrameDeck Studio.app** 移到废纸篓即可。用户创建的工程文件和导出的 PPT 不会随应用一起删除。
