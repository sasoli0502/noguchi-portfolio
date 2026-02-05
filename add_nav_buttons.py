import os
import re
from pathlib import Path

# ストーリーページのリスト
story_pages = [
    'baseball-story.html',
    'conversation-story.html', 
    'drinking-story.html',
    'games-story.html',
    'middle-way-story.html',
    'positive-story.html',
    'streaming-story.html',
    'subculture-story.html',
    'table-tennis-story.html',
    'tennis-story.html',
    'travel-story.html',
    'walking-story.html'
]

# CSSスタイルを追加する関数
def add_nav_styles(content):
    # すでにスタイルがある場合はスキップ
    if '.top-nav' in content or '.home-button' in content:
        return content
    
    # </style>の前にスタイルを挿入
    nav_css = '''
        .top-nav {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 100;
        }

        .home-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #00ffff;
            color: #00ffff;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .home-button:hover {
            background: rgba(0, 255, 255, 0.2);
            transform: translateX(-5px);
            box-shadow: 0 4px 15px rgba(0, 255, 255, 0.4);
        }
'''
    
    content = content.replace('</style>', nav_css + '    </style>')
    return content

# トップナビゲーションを追加する関数
def add_top_nav(content):
    # すでにトップナビがある場合はスキップ
    if '<nav class="top-nav">' in content:
        return content
    
    # <body>の直後に追加
    top_nav = '''<body>
    <nav class="top-nav">
        <a href="profile.html" class="home-button">🏠 トップへ戻る</a>
    </nav>'''
    
    content = content.replace('<body>', top_nav)
    return content

# ボトムナビゲーションを追加する関数
def add_bottom_nav(content):
    # </div>の前（最後のcontainer div）にボタンを追加
    # 既にボタンがある場合はスキップ
    if '🏠 トップへ戻る</a>' in content and content.count('🏠 トップへ戻る</a>') > 1:
        return content
    
    # 最後の</div>の前に追加
    # まず、最後の大きなコンテンツブロックを見つける
    pattern = r'(</body>)'
    
    bottom_nav = '''
        <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin: 3rem 0 2rem 0;">
            <a href="profile.html" class="home-button">🏠 トップへ戻る</a>
        </div>
    </div>
</body>'''
    
    # </div>\s*</body>を置換
    content = re.sub(r'</div>\s*</body>', bottom_nav, content, count=1, flags=re.MULTILINE)
    
    return content

# 各ページを処理
base_dir = Path(r'c:\Users\koyom\antigravity')

for page in story_pages:
    file_path = base_dir / page
    
    if not file_path.exists():
        print(f"Skipping {page} - file not found")
        continue
    
    print(f"Processing {page}...")
    
    # ファイルを読み込み
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # スタイルを追加
    content = add_nav_styles(content)
    
    # トップナビゲーションを追加
    content = add_top_nav(content)
    
    # ボトムナビゲーションを追加
    content = add_bottom_nav(content)
    
    # ファイルに書き戻し
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {page} updated")

print("\nAll story pages have been updated with navigation buttons!")
