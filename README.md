# How to generate images for personalized mugs

Note: these instructions are still not quite right - I'm not getting the same output size in pixels as we did last year.

1. Open the most recent .ai file in illustrator
2. Change the city name to the current summer school location
3. Export the file using the File > Export menu:
    - Name the output file `mug-aspp-01.png` and save it in the same directory as your script `mugs.py`
    - Choose the PNG (png) format to save as
    - You **MUST** check the box that says "Use Artboards" (this is below the format dropdown menu on the save dialog).
    - Select high resolution (300 ppi)
    - The other options can all be left as the default
4. Add a csv file `survey.csv` in the same spot as your script `mugs.py`. This csv should have a column named `Mugs` containing all the names to generate images for.
5. Run the python script `mugs.py`
