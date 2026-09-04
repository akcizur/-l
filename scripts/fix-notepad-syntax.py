from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
pattern = r"function note\(b,id\)\{.*?\nwindow\.noteSave="
replacement = '''function note(b,id){
  b.innerHTML = `<div class="pad">
    ${appMenu([["File","noteSave('\\${id}')"],["Open","noteOpen('\\${id}')"],["Clear","noteClear('\\${id}')"],["Help","dialog('Notepad Help','Ctrl+S uloží Notes.txt.')"]])}
    <textarea class="editor" id="ed_${id}"></textarea>
    <div class="status" id="ns_${id}">Ready</div>
  </div>`;
  const ed = document.getElementById(`ed_${id}`);
  ed.value = state.notes || (fs["C:\\\\My Documents\\\\Notes.txt"]?.x || "");
  ed.addEventListener("input", () => {
    state.notes = ed.value;
    const status = document.getElementById(`ns_${id}`);
    if (status) status.textContent = "Modified";
    save();
  });
}
window.noteSave='''
ns, count = re.subn(pattern, replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit('Notepad function was not found')
p.write_text(ns, encoding='utf-8')
print('patched', p)
