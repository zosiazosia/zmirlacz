class Counter:
    def __init__(self, inDir):
        self.came_in = 0
        self.came_out = 0
        self.reident_in = 0
        self.reident_out = 0
        self.are_inside = 0
        self.inDirection = inDir  # 'left or 'right'
        self.regular_left = 0
        self.regular_right = 0
        self.error_information = " "

    def come_in(self):
        self.came_in += 1
        self.are_inside += 1

    def come_out(self):
        self.came_out += 1
        self.are_inside -= 1

    def reid_in(self):
        self.reident_in += 1
        self.are_inside += 1

    def reid_out(self):
        self.reident_out += 1
        self.are_inside -= 1

    def getCameInString(self):
        return str(self.came_in)

    def getCameOutString(self):
        return str(self.came_out)

    def getReidentInString(self):
        return str(self.reident_in)

    def getReidentOutString(self):
        return str(self.reident_out)

    def getAreInsideString(self):
        return str(self.are_inside)

    def getInDirectionString(self):
        return self.inDirection

    def getRegularRightString(self):
        return str(self.regular_right)

    def getRegularLeftString(self):
        return str(self.regular_left)

    def generate_report(self, type):
        info = "came_in: " + self.getCameInString() + ", came_out: " + self.getCameOutString() + ", reid_in: " + \
               self.getReidentInString() + ", reid_out: " + self.getReidentOutString() + ", inside: " + self.getAreInsideString()
        report_eng = "Regular counter information: \n %s has come in and %s people has come out. \n" \
                     "Intelligent counter information: \n " \
                 "%s has been reidentified coming in and  %  has been reidentified coming out. " \
                 "Currently there are %s people inside. " \
                     % (self.getCameInString(), self.getCameOutString(), self.getReidentInString(),
                    self.getReidentOutString(), self.getAreInsideString())

        report_pl = "Tradycyjny licznik osób: \n %s osób weszło oraz %s osób wyszło. \n\n" \
                    "Inteligentny licznik osób: \n " \
                    "%s osób zostało zreidentyfikowanych wchodząc oraz %s osób zostało zreidentyfikowanych wychodząc. " \
                    "Obecnie w środku znajduje się %s osób. " \
                    % (self.getCameInString(), self.getCameOutString(), self.getReidentInString(),
                       self.getReidentOutString(), self.getAreInsideString())

        if type == 'eng':
            report = report_eng
        else:
            report = report_pl

        return report

    def increase_regular_left(self):
        self.regular_left += 1

    def increase_regular_right(self):
        self.regular_right += 1
