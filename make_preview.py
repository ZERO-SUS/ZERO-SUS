import re, pathlib
src = pathlib.Path(r"E:\websitelove\profile-3d-contrib\profile-bw-dual.svg").read_text(encoding="utf-8")

# Split the dual style into base (light) rules and the dark @media overrides.
style = re.search(r"<style>(.*?)</style>", src, re.DOTALL).group(1)
dark_block = re.search(r"@media \(prefers-color-scheme: dark\) \{(.*?)\}\s*$", style, re.DOTALL).group(1)
light_style = re.sub(r"@media \(prefers-color-scheme: dark\).*", "", style, flags=re.DOTALL)

def build(rules):
    return re.sub(r"<style>.*?</style>", "<style>" + rules + "</style>", src, count=1, flags=re.DOTALL)

pathlib.Path(r"E:\websitelove\_preview\light.svg").write_text(build(light_style), encoding="utf-8")
pathlib.Path(r"E:\websitelove\_preview\dark.svg").write_text(build(light_style + dark_block), encoding="utf-8")
print("wrote light.svg + dark.svg")
