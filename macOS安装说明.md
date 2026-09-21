# FrameDeck Studio v12.0.0 macOS 安装说明

## 适用范围

当前安装包：

- `FrameDeck-Studio-v12.0.0-macOS-arm64.dmg`
- `FrameDeck-Studio-v12.0.0-macOS-arm64.zip`

仅适用于 Apple Silicon 芯片的 Mac，例如 M1、M2、M3、M4。Intel Mac 暂不支持。

可在“终端”中执行以下命令确认机器架构：

```bash
uname -m
```

输出为 `arm64` 时可以安装；输出为 `x86_64` 时请勿安装此版本。

## 当前版本的重要说明

当前 macOS 版本为未签名、未经过 Apple 公证的内部测试版。请只从可信的官方测试渠道获取安装包。

首次启动时，macOS 可能提示无法验证开发者或无法检查软件是否包含恶意软件。这是因为当前版本尚未使用 Apple Developer ID 签名，并不等同于程序功能故障。

如果不信任安装包来源，请不要绕过 macOS 安全提示，也不要运行软件。

## 使用 DMG 安装

1. 双击 `FrameDeck-Studio-v12.0.0-macOS-arm64.dmg`。
2. 在打开的安装窗口中，将 `FrameDeck Studio.app` 拖入 `Applications`（应用程序）文件夹。
3. 等待复制完成。
4. 在 Finder 左侧推出 FrameDeck Studio 安装镜像。
5. 打开 Finder → 应用程序，确认存在 `FrameDeck Studio.app`。
6. 不要长期从 DMG 安装镜像内部直接运行程序。

## 首次启动

1. 在 Finder → 应用程序中找到 `FrameDeck Studio`。
2. 按住 `Control` 点击应用，选择“打开”。
3. 如果系统仍然阻止启动，点击“完成”，然后打开：

   `系统设置 → 隐私与安全性`

4. 向下滚动到“安全性”，找到 FrameDeck Studio 被阻止的信息。
5. 点击“仍要打开”。
6. 根据提示输入当前 Mac 的登录密码或使用 Touch ID。
7. 在再次出现的确认窗口中点击“打开”。

完成一次授权后，后续通常可以直接从“应用程序”启动。

请勿为了运行本软件而关闭整个 Gatekeeper，也不要执行来源不明的全局安全关闭命令。

## 使用 ZIP 包

ZIP 包仅作为备用分发方式。解压后，将 `FrameDeck Studio.app` 拖入“应用程序”文件夹，然后按照“首次启动”步骤授权。

如果 DMG 版本已经安装并测试通过，无需同时安装 ZIP 版本。

## 推荐的首次检查

启动后建议先使用少量 JPG、PNG 或 HEIC 图片检查：

1. 添加图片与自动分页。
2. 从 Finder 拖入图片。
3. 页面新增、复制、删除和移动。
4. 工程保存、关闭和重新打开。
5. PPT、PDF及页面图片导出。

确认少量图片操作正常后，再进行大批量图片测试。

## 常见问题

### 双击后没有反应或程序闪退

打开“终端”，执行：

```bash
"/Applications/FrameDeck Studio.app/Contents/MacOS/FrameDeck Studio" \
2>&1 | tee ~/Desktop/FrameDeck_DMG_first_run.log
```

日志会保存在桌面：

`FrameDeck_DMG_first_run.log`

请将日志和操作步骤提供给开发者排查。

### 系统仍然显示“已损坏”

请先确认：

- 安装包来自可信渠道；
- DMG已经完整下载；
- 当前Mac是ARM64架构；
- 应用已复制到“应用程序”文件夹，而不是直接从DMG运行。

不要直接执行网络上来源不明的 `xattr`、`spctl` 或关闭系统安全功能的命令。请联系开发者重新获取安装包或提供错误截图。

### Intel Mac无法运行

当前安装包文件名包含 `arm64`，不支持Intel Mac。需要单独提供 `x86_64` 或 `universal2` 构建。

## 卸载

1. 完全退出 FrameDeck Studio。
2. 在 Finder → 应用程序中，将 `FrameDeck Studio.app` 移到废纸篓。
3. 清倒废纸篓前请确认不再需要该版本。

卸载应用不会自动删除用户自行保存的工程、PPT、PDF或页面图片。

## 已验证环境

- macOS 26.6.1
- Apple M4
- 16 GB 内存
- ARM64
- DMG完整性验证通过
- 软件安装、启动及主要工程操作测试通过

已知限制：首次运行需要在“系统设置 → 隐私与安全性”中点击“仍要打开”。
