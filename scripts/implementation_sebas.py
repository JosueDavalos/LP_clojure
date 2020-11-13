from scripts.token import *
import ply.lex as lex


t_LISTA = r"^\(list\s((\s?((\"\w+\")|(\'[a-z])))+|(\s?[0-9]+)+)\)$"
# t_CONJUNTO = r""
# t_MAPA = r""
# t_VECTOR = r""
# t_FUNCTION = r"^\(defn\s\w+\s\[(\w)*(\s\w+)*\]\s?((\(.+\))|(\s\(.+\))*)\)$"
