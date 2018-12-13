# How to generate images for personalized mugs

1. Open the most recent .ai file in illustrator
2. Change the city name to the current summer school location
3. Export the file using the File > Export menu. You should expect the output .png file to have dimensions 2281 x 934 pixels. 
    - Name the output file `mug-aspp-01.png` and save it in the same directory as your script `mugs.py`
    - Choose the PNG (png) format to save as
    - You **MUST** check the box that says "Use Artboards" (this is below the format dropdown menu on the save dialog).
    - Select high resolution (300 ppi)
    - The other options can all be left as the default
4. Add a csv file `survey.csv` in the same spot as your script `mugs.py`. This csv should have a column named `Mugs` containing all the names to generate images for.
5. Run the python script `mugs.py`

Finally, double check that the output images look ok. Potential problems to look for:
- Any duplicate names, as the first image file will be overwritten by the (identical) second one. Make sure you order the right number!
- Names that are too long may appear truncated and may need special handling.
- Fonts specified are not installed on your machine. Either change the selected font in `mugs.py` or install the missing fonts onto your machine and teach matplotlib how to find them.
