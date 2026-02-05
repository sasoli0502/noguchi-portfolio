import re

# Read the file
with open(r'c:\Users\koyom\antigravity\profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match The Middle Way link
old_pattern = r'(&\s*The\s+<a href="middle-way-story\.html" class="hover-link" target="_blank"><span\s+class="highlight-blue">Middle Way</span></a>)'

# Replacement with wrapper and tap hint
new_text = '''& The 
                    <div class="clickable-hint-wrapper">
                        <a href="middle-way-story.html" class="hover-link" target="_blank"><span
                                class="highlight-blue">Middle Way</span></a>
                        <span class="tap-hint">👈 タップ</span>
                    </div>'''

# Replace
content = re.sub(old_pattern, new_text, content, flags=re.DOTALL)

# Write back
with open(r'c:\Users\koyom\antigravity\profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added tap hint to The Middle Way link!")
