import tomlkit

with open('requirements.txt', encoding='utf-8') as f:
    deps = [
        line.strip()
        for line in f
        if line.strip() and not line.strip().startswith('#')
    ]

with open('pyproject.toml', 'r', encoding='utf-8') as f:
    pyproject_data = tomlkit.parse(f.read())

pyproject_data['project']['dependencies'] = deps

with open('pyproject.toml', 'w', encoding='utf-8') as f:
    f.write(tomlkit.dumps(pyproject_data))

print("pyproject.toml dependencies successfully updated from requirements.txt")
