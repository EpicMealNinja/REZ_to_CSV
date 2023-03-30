import os
import PySimpleGUI as sg

#define main function
def main():
    #using PySimpleGUI find the folder with files to be converted
    layout = [[sg.Text("Select folder with files to be converted")],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Button("Ok")]]
    window = sg.Window("Folder Browser", layout)
    event, values = window.read()
    window.close()
    #get the path of the selected folder
    path = values[0]
    #get the list of files in the folder
    list_of_folders = os.listdir(path)
    #create a new folder to output to
    os.mkdir(path + "/../outputs")

    #loop through the list of folders
    for folder in list_of_folders:
        list_of_files = os.listdir(path + "/" + folder)
        #read the chunk.csv file in the folder with utf-8 encoding
        with open(path + "/" + folder + "/chunk.csv", encoding="utf-8") as f:
            chunk_file = f.read()
            #delete the first line of the chunk.csv file
            chunk_file = chunk_file.split("\n", 1)[1]
        #read the file csv file that starts with "AAHP" in the folder with utf-8 encoding
        for file in list_of_files:
            if file.startswith("AAHP"):
                file_name = file
                with open(path + "/" + folder + "/" + file, encoding="utf-8") as f:
                    csv_file = f.read()
                    #delete the first line of the csv file
                    csv_file = csv_file.split("\n", 1)[1]
                    csv_file = "Text, Chunk, Feature\n" + csv_file
        #split the csv file into a list of lines
        csv_file = csv_file.split("\n")
        #split the chunk.csv file into a list of lines
        chunk_file = chunk_file.split("\n")
        #loop through the list of lines in the chunk.csv file
        chunk_lines = []
        for line in chunk_file:
            #get rid of everything between quotation marks
            first = line.find('"')
            second = line.find('"', first + 1)
            line = line[second + 2:]
            #split the line by commas
            line = line.split(",")
            #add the split line to new variable
            chunk_lines.append(line)
        #loop through the list of lines in the csv file
        new_csv_file = []
        for line in csv_file:
            for chunk in chunk_lines:
                if line.find(chunk[0]) != -1:
                    line = line + "," + chunk[0]
                    chunk = chunk[1:]
                    #join the chunk back together
                    chunk = "".join(chunk)
                    #get rid of all commas
                    chunk = chunk.replace(",", "")
                    #add the chunk to the line
                    line = line + chunk

            new_csv_file.append(line)


        #write the new csv file to the outputs folder
        with open(path + "/../outputs/" + file_name, "w", encoding="utf-8") as f:
            for line in new_csv_file:
                f.write(line + "\n")

        

            
                

        

                
    







if __name__ == "__main__":
    main()