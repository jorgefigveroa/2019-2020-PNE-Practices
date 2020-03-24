class Seq:


    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
