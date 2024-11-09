<h1 align="center">
Surgical Video Annotation Software
</h1> 

<h1 align="center">
  <img src="surgui.png">
</h1>

## Description

A graphical video annotation tool, originally developed for labeling surgical videos. It is an easy to use software for labeling videos by creating customizable panels for:

- time-stamping the beginning and end of segments such as activities/tasks
- rating the videos/segments based on a custom scoring system
- extracting and saving important frames such as critical views
- pixel-level annotation of the images by opening in [labelme](https://github.com/wkentaro/labelme/) software

## Installation for the DISE project (verified on Mac)
- Download \& install Anaconda
  - [Anaconda](https://www.anaconda.com/download/success)
  - Open the Anaconda-Navigator app
  - Update Anaconda-Navigator if necessary
- Download \& install VLC media player
  - [Mac install (Universal Binary)](https://get.videolan.org/vlc/3.0.21/macosx/vlc-3.0.21-universal.dmg) 
  - [Windows install](https://apps.microsoft.com/detail/xpdm1zw6815mqm?ocid=webpdpshare)

- Recommended:
  - Download [GitHub Desktop](https://desktop.github.com/download/)
  - Login to GitHub Desktop
  - In this repo, click the green code button, then click open with GitHub Desktop
- Otherwise:
  - Download the SurgUI-master zipped repository [here](https://github.com/wzkariampuzha/SurgUI/archive/refs/heads/master.zip) 
  - Unzip it

 - Open the terminal app (Mac) or Windows powershell:
    - Now you need to navigate to the folder where you copied the SurgUI-master folder 
    - Eg. If you copied the SurgUI-master folder	 to `C:\Users\SurgUI-master` then in the command line write `cd C:\Users\SurgUI-master`. To copy the pathname of your SurgUI folder on macOS, see [here](https://support.apple.com/en-gb/guide/mac-help/mchlp1774/mac#:~:text=Show%20the%20path%20to%20a,show%20the%20path%20bar%20momentarily.).  
    - See this example: 
    - <img src="change-working-directory-example.png">
    - ```shell
        cd path/to/SurgUI-master
        ```
   - e.g. mine is under `cd /Users/wzk/Documents/GitHub/SurgUI`
    Then run these commands:
     - ```shell
        conda env create --file environment.yml
        conda activate surgui-venv
        ```
    Install the software:
    - ```shell
        python setup.py install
      ```

## Videos
Download videos from

## Usage
- Open VLC media player

- Open terminal and run the following command (update the path to where your own SurgUI-master folder is located):
    ```shell
    conda activate surgui-venv
    cd path/to/SurgUI-master
    python surgui
    ```

### Segment Rating:
For annotating the start and end of segments, first click File then "Add Rating Panel" then select the `RatingsPanel-Anatomy.txt` file. Then click File, "Add Timestamp Panel", select `TimeStampPanel-ObstructedViews.txt`. Then click File and find and open a video. For each video that is playing, a folder with the same name is created in “outputs” directory.

#### Rating System: 
Every time you see a new anatomical segment, mark the start time, play through *until you can identify that you are no longer in the same anatomical segment*, mark the end time, then click a rating:
- 1: No significant secretions 
- 2: Secretions that don't impeded visualization 
- 3: Secretions that impede visualization, but don't completely block your view 
- 4: Secretions that completely block your view, making it difficult to get a good assessment
- 5: Nothing, do not use this rating

Every anatomical segment, take a screenshot at some point and then use the labelme software to draw out secretions that obscure the lens. Secretions are labeled as "secretionstissue" if on the soft tissue or "secretionslens" if on the lens of the scope. You should draw polygons around these secretions. 


#### Obstructed Views:
- Use this time stamp panel to mark any time points where the view is so obscured that you cannot ascertain which anatomical structure is being visualized.
- A few frames or less than a second of obstruction does not need to be marked, however if there is a significant period of time without visualization, you should mark it.
- Use this even when you know that you are in an anatomical segment (because the camera has not moved), but you could not tell which segment you are in solely from the frame.
- - Example: you are in the oropharynx and then view gets obstructed for 10 seconds before emerging in the tongue level. You should mark the end of the oropharynx level as when you emerged into seeing the tongue, but the entire 10 seconds of obstructed view should be flagged as obstructed view.

#### Saved Annotations
- The saved images and the .json files from labelme annotations are stored in `images` folder for each video.
- **Check** your annotation files for completeness
