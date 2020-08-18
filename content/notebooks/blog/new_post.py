import pathlib
from datetime import datetime
import shutil

curdir = pathlib.Path().absolute()
blogdir = curdir
while blogdir.name != 'DeanLa.github.io':
    blogdir = blogdir.parent

now = datetime.now()
shortdt = now.strftime("%y%m%d")
longdt = now.strftime("%Y-%m-%d %H:%M")
posts = blogdir / 'content' / 'posts'
nbs = blogdir / 'content' / 'notebooks'
base_nb = nbs / 'template' / 'main.ipynb'

# Create new md file in content/posts
# Create new dir with same name in notebooks, inside it put "main.ipynb"
# Create new empty image, maybe with a name or something

md_tmplt = f'''Title: {{title}}
Date: {longdt}
Modified: {longdt}
Status: published
Category: {{category}}
Tags: {{tags}}
Slug: {{slug}}
Author: Dean
og_image: img/img_posts/{{slug}}.png
Summary: 

'''

def new_post(title, slug=None, tags=None, category=None):
    slug = slug or title.replace(' ', '-').lower()
    category = category or "Python"
    tags = tags or []
    tags = ", ".join(tags)
    filename = f'{shortdt}_{slug.replace("-", "_")}'
    new_nb = nbs / f'{shortdt}_{slug.replace("-","_")}' / 'main.ipynb'
    folder = new_nb.parent
    folder.mkdir(exist_ok=True, parents=True)
    header = md_tmplt.format_map(locals())
    content = r'{%' + f' notebook {folder.name}/main.ipynb ' + r'%}'
    content = header + content
    if new_nb.exists():
        raise FileExistsError(f'{new_nb} exists')
    shutil.copy(base_nb, new_nb)
    with open((posts / filename).with_suffix('.md'), 'w') as f:
        f.write(content)

new_post('Time Deltas', tags=['pandas','datetime'])
print()
