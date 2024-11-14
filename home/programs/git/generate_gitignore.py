import urllib
import urllib.request

req = urllib.request.Request(
    "https://www.toptal.com/developers/gitignore/api/macos,python,jetbrains,django,linux,vim",
    headers={"user-agent": "curl/8.10.1"},
)
with urllib.request.urlopen(req) as response:
    with open("gitignore_global.nix", "wb") as nix_file:
        nix_file.write(b"""
{
  programs.git.ignores = [ 
        """)
        line: bytes = response.readline()
        while line:
            if not line.startswith(b"#") and line.rstrip():
                line = b'"%b"\n' % (line.rstrip(),)
            nix_file.write(line)
            line = response.readline()

        nix_file.write(b"""
".nvim.lua"
".nvimrc"
".direnv"
""")
        nix_file.write(b"""
  ];
}
""")
