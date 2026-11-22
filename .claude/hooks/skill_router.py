"""UserPromptSubmit hook: point Claude to a superpowers skill when the prompt asks for it.

Reads the hook JSON on stdin and, on a keyword match, prints additionalContext.
Prints nothing otherwise, so ordinary prompts cost no tokens.
"""
import json
import re
import sys
import unicodedata

RULES = [
    ("superpowers:systematic-debugging",
     r"\b(error|errores|bug|bugs|falla|fallo|fallan|roto|rota|broken|404|crash|traceback|exception|"
     r"no compila|no funciona|no carga|no se ve|test(s)? en rojo|failing)\b"),
    ("superpowers:brainstorming",
     r"\b(crea una pagina|nueva pagina|nueva feature|nueva funcion|nueva funcionalidad|"
     r"disena|nuevo tema|new feature|new page)\b"),
]


def plain(text):
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def route(prompt):
    p = plain(prompt)
    return [skill for skill, pat in RULES if re.search(pat, p)]


def main():
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", "ignore") or "{}")
    except ValueError:
        return
    skills = route(data.get("prompt", ""))
    if not skills:
        return
    note = ("Skill router: this prompt matches " + ", ".join(skills)
            + ". Invoke it with the Skill tool before acting, unless it is plainly irrelevant.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                             "additionalContext": note}}))


if __name__ == "__main__":
    assert route("La página da un 404") == ["superpowers:systematic-debugging"]
    assert route("Diseña una página nueva") == ["superpowers:brainstorming"]
    assert route("Resuelve el problema 3") == []
    main()
