# 小藝繪本：階段 0 試讀網站

網站入口：https://ellis1004.github.io/xiaoyi-books/ 。實際發布狀態與檢查結果記在專案 REPORT.md。

本網站沿用總編輯提供的 index.html 版面和文案。本輪先提供造型 A；B、C、D 仍顯示原稿的「插圖製作中」，等 A 驗收後才製作。
Ellis 本輪另行核准兩處 CSS 修正：手機造型選項不再撐出輸入卡片，以及把太陽的絕對定位只套在首頁裝飾，避免預購按鈕壓住價格。HTML 內文與 JavaScript 維持原稿。

## 換圖片

每一造型的網站圖放在以下位置，檔名大小寫必須一致：

```text
web/img/grow/A/cover.webp
web/img/grow/A/T1.webp
web/img/grow/A/T2.webp
web/img/grow/A/T3.webp
web/img/grow/A/T4.webp
web/img/grow/A/T5.webp
```

後續 B、C、D 把路徑中的 A 換成對應字母。每張為 1080 × 1080，檔案必須小於 300,000 bytes；圖片本身不放文字，網站會疊上孩子的名字與文稿。

原圖在專案 images/grow/；另外有 upscaled/ 的 2550 × 2550 印刷參考副本，使用 Pillow LANCZOS 放大。網站使用壓縮 WebP，不用印刷副本。兩款封面各存 cover_v1.webp、cover_v2.webp，目前 cover.webp 與款一相同；要換款二時，複製 cover_v2.webp 覆蓋 cover.webp 即可，其他頁不動。

## 填預購網址與信箱

設定沿用原稿，放在 **web/index.html 最下方的 script**，不是另外的 config.js。搜尋：

```javascript
const PREORDER_URL = "";
const CONTACT_EMAIL = "";
```

把 Google 表單的完整 https 網址填入 PREORDER_URL 的引號裡，信箱填入 CONTACT_EMAIL。儲存並重新部署後生效。

PREORDER_URL 空白時，按鈕顯示「預購表單準備中」，不能送出訂單。網址填好後，原稿會附帶 name 和 look 兩個參數。Google 表單真正的預填欄位 entry 編號仍需 Ellis 設定；目前不會自動對應 Google 表單欄位。不要把家長資料或孩子訂單檔上傳到這個公開儲存庫。

原稿沒有 GA_ID 設定或追蹤程式，本次不自行新增；若需要統計，先由總編輯確認後再加入。

## 字型

使用 assets/fonts/ 下的 jf open 粉圓 WOFF2，單一字重 400，授權保存在 ofl.txt。font.css 的 @font-face 以 unicode-range 分段載入，讓一般頁面只下載用到的中文字，輸入其他名字時再載入需要的字段。沒有 Google Fonts 連結。

本機可以直接開 web/index.html 查看；正式驗證使用本機網站服務及 Playwright。完整網站沒有後端、會員、購物車或資料庫。

## GitHub Pages 部署與更新

公開儲存庫為 ellis1004/xiaoyi-books。儲存庫只包含 web/ 網站及 .github/workflows/pages.yml，不包含 orders/、原始插圖或整個雲端硬碟專案。

1. 在 GitHub 的 ellis1004/xiaoyi-books 修改 web/ 下對應的檔案，提交到 main。
2. Actions 裡的 Publish Xiaoyi Books 會發布 web/；等待綠色完成，再開網站重新整理。
3. Settings → Pages 的發布來源設為 GitHub Actions。工作流程只上傳 web/。

本機發布副本位於專案 _publish/xiaoyi-books/。雲端硬碟的 web/ 改完後，須同步到這個副本、提交並推送，才會更新線上；單純修改雲端硬碟不會自動發布。

部署流程依 [GitHub Pages 官方文件](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)；工作流程已固定使用查證過的官方 Actions 版本。

## 預覽與檢查記錄

手機、電腦截圖放在專案 previews/web/mobile.png、desktop.png；互動與圖片載入結果在同資料夾 verification.json。七張原圖的聯絡表與自檢放在 previews/grow/。
