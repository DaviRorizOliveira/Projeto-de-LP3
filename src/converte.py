class Converte:
    @staticmethod 
    def animal(a):
        match a:
            case 0:
                return 'vaca'

            case 1:
                return 'galinha'

            case 2:
                return 'ovelha'
    @staticmethod 
    def produto(a):
        match a:
            case 0:
                return "leite"
            case 1:
                return "ovos"
            case 2:
                return "lã"