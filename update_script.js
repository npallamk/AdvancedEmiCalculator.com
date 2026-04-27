const fs = require('fs');
const path = require('path');

const dirPath = __dirname;
const adBlock = `  <!-- ══ AD CARD — above footer ══ -->
  <div class="ad-card" style="margin-bottom: 14px;">
    <div class="ad-label">Advertisement</div>
    <div style="padding:4px 10px 10px">
      <ins class="adsbygoogle"
           style="display:block;min-height:90px"
           data-ad-client="ca-pub-3261920810785932"
           data-ad-slot="auto"
           data-ad-format="auto"
           data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
  </div>`;

let modifiedCount = 0;

fs.readdirSync(dirPath).forEach(file => {
    if (!file.endsWith('.html')) return;
    
    const filePath = path.join(dirPath, file);
    let originalContent = fs.readFileSync(filePath, 'utf8');
    let content = originalContent;
    
    // 1. replace 'Made with...' text
    content = content.replace(/(\&copy\;\s*2026\s*<strong>.*?<\/strong>)\s*\&middot\;\s*Made with\s*<span[^>]*>[^<]*<\/span>\s*in\s*India/ig, '$1');

    // 2. add ad-card above footer if not index.html
    if (file !== 'index.html') {
        if (!content.includes('<!-- ══ AD CARD — above footer ══ -->')) {
            content = content.replace('<!-- SITE FOOTER -->', adBlock + '\n\n  <!-- SITE FOOTER -->');
        }
    }
    
    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        modifiedCount++;
        console.log(`Modified ${file}`);
    }
});

console.log(`Done. Modified ${modifiedCount} files.`);
