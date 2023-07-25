class cricket_rules:
    #runs = 1000
    #overs = 50
    #balls = 6

    def batsman(self,name,matches,runs,avg,half,cen,sr):
        self.name = name
        self.matches = matches
        self.runs = runs
        self.avg = avg
        self.half = half
        self.cen = cen
        self.sr = sr
        print("player:",name)
        print("runs:",runs)
        print("avg:",runs/matches)
        print("half:",half)
        print("cen:",cen)
        print("sr:",sr)

ishan = cricket_rules()
vk = cricket_rules()
dhoni = cricket_rules()
rohit = cricket_rules()
rahane = cricket_rules()
jaddu = cricket_rules()
aswin = cricket_rules()
siraj = cricket_rules()
shami = cricket_rules()
mukesh = cricket_rules()

ishan.batsman("ishan",20,300,"avg",2,1,130)

ishan.batsman("vk",200,10000,"avg",29,12,150)
dhoni.batsman("dhoni",500,40000,"avg",52,18,150)