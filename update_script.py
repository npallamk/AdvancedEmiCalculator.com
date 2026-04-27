import os
import re

dir_path = r"c:\Users\Nithin\Downloads\index_18-04-2026_Manual_Edit_Origin_15-04-2026"

ad_block = """  <!-- ══ AD CARD — above footer ══ -->
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
  </div>"""

modified_count = 0

for f in os.listdir(dir_path):
    if not f.endswith(".html"): continue
    
    p = os.path.join(dir_path, f)
    with open(p, "r", encoding="utf-8") as file:
        original_content = file.read()
        
    content = original_content
    
    # 1. replace 'Made with...' text
    content = re.sub(
        r'(\&copy\;\s*2026\s*<strong>.*?</strong>)\s*\&middot\;\s*Made with\s*<span[^>]*>[^<]*</span>\s*in\s*India',
        r'\1',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 2. add ad-card above footer if not index.html
    if f != "index.html":
        # Check if ad-card already added right before footer
        if "<!-- ══ AD CARD — above footer ══ -->" not in content:
            # We want to place it right before <!-- SITE FOOTER -->
            content = content.replace("<!-- SITE FOOTER -->", ad_block + "\n\n  <!-- SITE FOOTER -->")
            
    if content != original_content:
        with open(p, "w", encoding="utf-8") as file:
            file.write(content)
        modified_count += 1
        print(f"Modified {f}")
        
print(f"Done. Modified {modified_count} files.")
