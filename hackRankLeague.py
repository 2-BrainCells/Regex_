import re

langs = list("C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(":"))

N = int(input())
for _ in range(N):
    s=input()
    id, l = re.findall(r"^\d{4,5}\s\w+",s)[0].split()
    if l in langs:
        print("VALID") 
    else:
        print("INVALID")