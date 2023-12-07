

class RegexBasic():

    def Normalize(self,_str):
        replacements = (
            ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n"),   
            ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"), ("Ñ", "N"),
            (" -", ""), (" ", "_"), ("-", "")
        ) 
        for a, b in replacements:
            _str = _str.replace(a, b)
        return _str