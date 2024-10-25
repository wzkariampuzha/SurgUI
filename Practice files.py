
#f.write("Label={} | Rating={} | Start={} | End={} \n".format(task_name, score, starting_time, ending_time))


def saveRatingPanel(self, panel_index, i):
    if self.save_directory:
        form_title = self.form_title[panel_index].text()
        # If an existing rating file exists, load it and update the ratings
        rating_file = "{}/{}_scores.txt".format(self.save_directory,form_title)
        if os.path.exists(rating_file):
            with open(rating_file) as f:
                lines = f.readlines()
                #This will save a list of dicts with the following save format
                new_lines = [] # ?
                # The save format of a rating file is
                # "Label={} | Rating={} | Start={} | End={}"
                # This unpacks the lines into a dict
                for line in lines:
                    line_dict = dict()
                    for entry in line.split("|"):
                        key, value = entry.split("=")
                        line_dict[key] = value
                    new_lines.append(line_dict)
            
            # Task index refers to a grouping of start time, end time, and a rating on the panels (which is  contained in groupButtonlist)
            for task_index in range(len(self.groupButtonlist[self.panel_index])):
                # This checks if the task on the panel (e.g. Velopharynx initial view) is the same as one of the tasks in the saved rating score file
                if self.tasklist[self.panel_index][task_index].text() in [line_dict["Label"] for line_dict in new_lines]:
                    # The purpose of this next section is to update the rating panel that you are opening up in SurgUI with the scores and times that you have saved within the rating score file
                    for line_dict in new_lines:
                        if line_dict["Label"] == self.tasklist[self.panel_index][task_index].text():
                            self.startingTimelist[self.panel_index][i] = line_dict["Start"]
                            self.endingTimelist[self.panel_index][i] = line_dict["End"]
                            # Set the rating score
                            for j in range(len(self.ratingButtonslist[self.panel_index][i])):
                                # Check if the score is a valid number before converting
                                if score.strip().isdigit():  # Check if score is numeric
                                    if int(self.ratingButtonslist[self.panel_index][i][j].text()) == int(line_dict["Rating"]):
                                        self.ratingButtonslist[self.panel_index][i][j].setChecked(True)
                                else:
                                    # Handle case when score is 'Not rated' or any other non-numeric value
                                    print(f"Skipping invalid score: {score}")
                

                # Rewrite the file with the updated lines
                with open(
                    "{}/{}_scores.txt".format(
                        self.save_directory,
                        self.form_title[self.panel_index].text(),
                    ),
                    "w",
                ) as f:
                    f.writelines(new_lines)
            else:
                if self.save_directory:
                    with open("{}/{}_scores.txt".format(self.save_directory, self.form_title[self.panel_index].text()), "a") as out:

                        for i in range(len(self.groupButtonlist[self.panel_index])):
                            starting_time = self.startingTimelist[self.panel_index][i].text()
                            ending_time = self.endingTimelist[self.panel_index][i].text()
                            score = None

                            # Check which radio button is selected and get the score
                            for j in range(len(self.ratingButtonslist[self.panel_index][i])):
                                if self.ratingButtonslist[self.panel_index][i][j].isChecked():
                                    score = self.ratingButtonslist[self.panel_index][i][j].text()

                            # Only write valid entries (if a rating and timestamps are set)
                            if starting_time != "0" and ending_time != "0" and score is not None:
                                out.write("{} : {} | Time: {} to {}\n".format(
                                    self.tasklist[self.panel_index][i].text(), score, starting_time, ending_time))
            



def save_rating_entry(self, panel_index, i):
        form_title = self.form_title[panel_index].text()
        task_name = self.tasklist[panel_index][i].text()
        starting_time = self.startingTimelist[panel_index][i].text()
        ending_time = self.endingTimelist[panel_index][i].text()

        # Get the selected rating
        score = None
        for j in range(len(self.ratingButtonslist[panel_index][i])):
            if self.ratingButtonslist[panel_index][i][j].isChecked():
                score = self.ratingButtonslist[panel_index][i][j].text()

        # Save the entry to a file
        rating_file = "{}/{}_scores.txt".format(self.save_directory,form_title)

        with open(rating_file, "a") as f:
            f.write("Label={} | Rating={} | Start={} | End={} \n".format(task_name, score, starting_time, ending_time))

        # Check if saveEntryBtn exists before trying to disable it
        if self.saveEntryBtn[panel_index] and len(self.saveEntryBtn[panel_index]) > i:
            self.saveEntryBtn[panel_index][i].setEnabled(False)

if self.save_directory:
            if os.path.exists("{}/{}_scores.txt".format(self.save_directory,
                                                    self.form_title[self.panel_index].text())):
                # load previous ratings
                with open("{}/{}_scores.txt".format(self.save_directory,
                                                    self.form_title[self.panel_index].text()),"r",) as f:
                    lines = f.readlines()
                    new_lines = []
                    for line in lines:
                        rating_item = line.split(" : ")[0]
                        details = line.strip().split(" : ")[1]
                        existing_score, existing_times = details.split(" | ") if " | " in details else (details, "Not set")

                        if len(line.split(" : ")) == 2:
                            score = line.split(" : ")[1]

                            for i in range(len(self.groupButtonlist[self.panel_index])):
                                # This checks if the task on the panel (e.g. Velopharynx initial view) is the same as one of the tasks in the saved rating score file
                                if self.tasklist[self.panel_index][i].text() == rating_item:
                                    # This iterates through 
                                    for j in range(len(self.ratingButtonslist[self.panel_index][i])):
                                        # Check if the score is a valid number before converting
                                        if score.strip().isdigit():  # Check if score is numeric
                                            if int(self.ratingButtonslist[self.panel_index][i][j].text()) == int(score):
                                                self.ratingButtonslist[self.panel_index][i][j].setChecked(True)
                                        else:
                                            # Handle case when score is 'Not rated' or any other non-numeric value
                                            print(f"Skipping invalid score: {score}")

                                    # Update timestamp alongside score
                                    new_lines.append(f"{rating_item} : {score} | {self.startingTimelist[self.panel_index][i].text()} to {self.endingTimelist[self.panel_index][i].text()}")

                # Rewrite the file with the updated lines
                with open(
                    "{}/{}_scores.txt".format(
                        self.save_directory,
                        self.form_title[self.panel_index].text(),
                    ),
                    "w",
                ) as f:
                    f.writelines(new_lines)
            else:
                if self.save_directory:
                    with open("{}/{}_scores.txt".format(self.save_directory, self.form_title[self.panel_index].text()), "a") as out:

                        for i in range(len(self.groupButtonlist[self.panel_index])):
                            starting_time = self.startingTimelist[self.panel_index][i].text()
                            ending_time = self.endingTimelist[self.panel_index][i].text()
                            score = None

                            # Check which radio button is selected and get the score
                            for j in range(len(self.ratingButtonslist[self.panel_index][i])):
                                if self.ratingButtonslist[self.panel_index][i][j].isChecked():
                                    score = self.ratingButtonslist[self.panel_index][i][j].text()

                            # Only write valid entries (if a rating and timestamps are set)
                            if starting_time != "0" and ending_time != "0" and score is not None:
                                out.write("{} : {} | Time: {} to {}\n".format(
                                    self.tasklist[self.panel_index][i].text(), score, starting_time, ending_time))



def add_time_panel_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Text", filter="Text files (*.txt)"
        )

        if filename != "":
            title = str(os.path.basename(filename)).split(".")[0]
            with open(filename) as f:
                lines = f.read().splitlines()
            print("Opened time panel:", title)

            self.num_panels += 1

            self.panel_index = self.num_panels

            self.tasklist[self.panel_index] = []
            self.startingButtonlist[self.panel_index] = []
            self.startingTimelist[self.panel_index] = []
            self.endingButtonlist[self.panel_index] = []
            self.endingTimelist[self.panel_index] = []
            self.saveEntryBtn[self.panel_index] = []
            self.clearEntryBtn[self.panel_index] = []
            # self.scoretime[self.panel_index] = []

            self.groupbox[self.panel_index] = QGroupBox()
            self.formLayout[self.panel_index] = QFormLayout()

            self.form_title[self.panel_index] = QLabel(title)
            self.form_title[self.panel_index].setStyleSheet("color: white")
            self.form_title[self.panel_index].setAlignment(Qt.AlignCenter)
            self.form_title[self.panel_index].setFont(
                QFont("Times", 12, weight=QFont.Bold)
            )
            self.panelRemoveBtn[self.panel_index] = QPushButton("Exit")
            self.panelRemoveBtn[self.panel_index].clicked.connect(
                partial(self.onpanelRemoveBtnClicked, self.panel_index)
            )

            self.formLayout[self.panel_index].addRow(
                self.form_title[self.panel_index]
            )  # , self.panelRemoveBtn[self.panel_index])

            for i, line in enumerate(lines):
                line = line.split("#")

                self.tasklist[self.panel_index].append(QLabel(line[0]))
                self.tasklist[self.panel_index][i].setStyleSheet(
                    "background-color: black ; color: white"
                )
                self.tasklist[self.panel_index][i].setFont(
                    QFont("Times", 10, weight=QFont.Bold)
                )
                self.tasklist[self.panel_index][i].setWordWrap(True)
                self.startingButtonlist[self.panel_index].append(QPushButton("starts"))
                self.startingButtonlist[self.panel_index][i].setFixedWidth(50)
                self.startingTimelist[self.panel_index].append(QLabel("0"))
                self.startingTimelist[self.panel_index][i].setStyleSheet("color: white")
                self.startingButtonlist[self.panel_index][i].clicked.connect(
                    partial(self.onstartbuttonClicked, self.panel_index, i)
                )
                self.endingButtonlist[self.panel_index].append(QPushButton("ends"))
                self.endingButtonlist[self.panel_index][i].setFixedWidth(50)
                self.endingTimelist[self.panel_index].append(QLabel("0"))
                self.endingTimelist[self.panel_index][i].setStyleSheet("color: white")
                self.endingButtonlist[self.panel_index][i].clicked.connect(
                    partial(self.onendbuttonClicked, self.panel_index, i)
                )
                if len(line) == 3:
                    self.startingButtonlist[self.panel_index][i].setToolTip(line[1])
                    self.endingButtonlist[self.panel_index][i].setToolTip(line[2])
                self.saveEntryBtn[self.panel_index].append(QPushButton("save"))
                self.clearEntryBtn[self.panel_index].append(QPushButton("clear"))
                self.saveEntryBtn[self.panel_index][i].setFixedWidth(50)
                self.clearEntryBtn[self.panel_index][i].setFixedWidth(50)
                self.saveEntryBtn[self.panel_index][i].setEnabled(False)
                self.saveEntryBtn[self.panel_index][i].clicked.connect(
                    partial(self.saveTimeStampPanel, self.panel_index, i)
                )
                self.clearEntryBtn[self.panel_index][i].setEnabled(False)
                self.clearEntryBtn[self.panel_index][i].clicked.connect(
                    partial(self.onclearEntryBtnClicked, self.panel_index, i)
                )

                self.formLayout[self.panel_index].addRow(
                    self.tasklist[self.panel_index][i]
                )
                self.formLayout[self.panel_index].addRow(
                    self.startingButtonlist[self.panel_index][i],
                    self.startingTimelist[self.panel_index][i],
                )
                self.formLayout[self.panel_index].addRow(
                    self.endingButtonlist[self.panel_index][i],
                    self.endingTimelist[self.panel_index][i],
                )
                self.formLayout[self.panel_index].addRow(
                    self.saveEntryBtn[self.panel_index][i],
                    self.clearEntryBtn[self.panel_index][i],
                )

            self.groupbox[self.panel_index].setLayout(self.formLayout[self.panel_index])
            self.scroll[self.panel_index] = QScrollArea()
            self.scroll[self.panel_index].setWidget(self.groupbox[self.panel_index])
            self.scroll[self.panel_index].setWidgetResizable(True)
            self.scroll[self.panel_index].setFixedWidth(300)
            self.scroll[self.panel_index].setFocusPolicy(Qt.StrongFocus)
            self.mainLayout.addWidget(self.scroll[self.panel_index])

        # If an existing timestamp file exists, load it and update the timestamps on the panel
        if self.save_directory:
            timestamp_file = "{}/{}_timestamps.txt".format(self.save_directory, self.form_title[panel_index].text())
            if os.path.exists(timestamp_file):
                with open(timestamp_file) as f:
                    lines = f.readlines()
                    #This will save a list of dicts with the following save format
                    new_lines = [] # ?
                    # The save format of a timestamp file is
                    # "Label={} | Start={} | End={}"
                    # This unpacks the lines into a dict
                    for line in lines:
                        line_dict = dict()
                        for entry in line.split("|"):
                            key, value = entry.split("=")
                            line_dict[key] = value
                        new_lines.append(line_dict)
                
                # Task index refers to a grouping of start time, end time, and a rating on the panels (which is  contained in groupButtonlist)
                for task_index in range(len(self.groupButtonlist[self.panel_index])):
                    # This checks if the task on the panel (e.g. Velopharynx initial view) is the same as one of the tasks in the saved rating score file
                    if self.tasklist[self.panel_index][task_index].text() in [line_dict["Label"] for line_dict in new_lines]:
                        # The purpose of this next section is to update the rating panel that you are opening up in SurgUI with the scores and times that you have saved within the rating score file
                        for line_dict in new_lines:
                            if line_dict["Label"] == self.tasklist[self.panel_index][task_index].text():
                                self.startingTimelist[self.panel_index][i] = line_dict["Start"]
                                self.endingTimelist[self.panel_index][i] = line_dict["End"]


    def save_entry(self, panel_index, i):
        self.saveEntryBtn[panel_index][i].setEnabled(False)

        form_title = self.form_title[panel_index].text()
        task_name = self.tasklist[panel_index][i].text()
        starting_time = self.startingTimelist[panel_index][i].text()
        ending_time = self.endingTimelist[panel_index][i].text()
        
        # if there is a rating button then run this
        try self.ratingButtonslist[panel_index][i]:
            # Get the selected rating
            score = None
            for j in range(len(self.ratingButtonslist[panel_index][i])):
                if self.ratingButtonslist[panel_index][i][j].isChecked():
                    score = self.ratingButtonslist[panel_index][i][j].text()
            
            # Save the entry to a file
            rating_file = "{}/{}_ratings.txt".format(self.save_directory, form_title)
            with open(rating_file, "a") as f:
                f.write("Label={} | Rating={} | Start={} | End={} \n".format(task_name, score, starting_time, ending_time))
            
            # Check if saveEntryBtn exists before trying to disable it
            if self.saveEntryBtn[panel_index] and len(self.saveEntryBtn[panel_index]) > i:
                self.saveEntryBtn[panel_index][i].setEnabled(False)
        # If it is timestamp, run this
        except: 
            # Save the timestamp entry to a file
            timestamp_file = "{}/{}_timestamps.txt".format(self.save_directory, form_title)
            with open(timestamp_file, "a") as f:
                f.write("Label={} | Start={} | End={}\n".format(task_name, starting_time, ending_time))

            # Disable the buttons after saving
            self.clearEntryBtn[panel_index][i].setEnabled(True)