from PIL import Image
import os

from init import Root

# 1. 读取转换后的P模式图
p_img = Image.open(Root / 'test11图片/typicalImage/globe_wais.png')
palette_list = p_img.getpalette()
trans_idx_old = p_img.info.get("transparency")  # 原来的透明索引：4
used_indices = set(p_img.getdata())  # 原来的像素索引：{0,1,2,3,4,5,6}

# 2. 调整调色板顺序：把透明色移到索引0的位置
# 步骤1：提取透明色的RGB值
trans_rgb = (
    palette_list[trans_idx_old * 3],
    palette_list[trans_idx_old * 3 + 1],
    palette_list[trans_idx_old * 3 + 2]
)
# 步骤2：重新排列调色板 → [透明色, 原来的0,1,2,3,5,6]
new_palette = []
new_palette.extend(trans_rgb)  # 索引0：透明色
for idx in used_indices:
    if idx != trans_idx_old:
        r = palette_list[idx * 3]
        g = palette_list[idx * 3 + 1]
        b = palette_list[idx * 3 + 2]
        new_palette.extend([r, g, b])

# 3. 更新像素索引值：建立「旧索引→新索引」的映射
# 旧索引4 → 新索引0
# 旧索引0 → 新索引1，旧索引1→新索引2 ... 旧索引6→新索引6
index_map = {trans_idx_old: 0}
new_idx = 1
for old_idx in sorted(used_indices):
    if old_idx != trans_idx_old:
        index_map[old_idx] = new_idx
        new_idx += 1

# 4. 批量替换所有像素的索引
new_pixel_data = [index_map[old_idx] for old_idx in p_img.getdata()]
p_img.putdata(new_pixel_data)

# 5. 重新设置调色板和透明索引
p_img.putpalette(new_palette)
p_img.info["transparency"] = 0  # 透明索引改为0

# 6. 优化压缩保存（关键！和之前的体积优化一致）
p_img.save(
    Root / 'test11图片/typicalImage/2.png',
    format="PNG",
    optimize=True,
    compress_level=9
)
