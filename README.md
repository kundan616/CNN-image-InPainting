# CNN-image-InPainting

starter code for creating your own image in painting 

STEPS:<br>
1. create a dataset of your own images or download open source any dataset and put it in a folder.<br>
2. give the variable  image_folder path to the folder containing images (eg. image_folder='val2017/') in the first cell<br>
3. create two folders named pro and norm for storing processed immages and run the first cell<br>
4. it will put black patches randomly accross the images representing missing parts of the image<br>


<i>original image</i>
<img src="/image/17.jpg">
<i>patched image</i>
<img src="/image/17_p.jpg">

5. the next cell is creating the autoencoder network , change the architecture if you want or use the ine provided<br>
6. this cell is spliting the data in training and test , I used a subset of COCO dataset containing 5000 images so im doing the split on 5000 images , do the split as per your dataset , len(data) to find out the total number of example PS: data array contains patched images (input) ,norm contains normal images (output label)<br>
7. if you want to use tensorboard the execute next three cells or ignore them if you aren't planning on using tensorboard<br>
8. run the next cell and train the network (remove callback attribute if not using tensorboard) change epochs and batch according to your requirements and tuning <br>
9. next two cells are for testing the results produced by the network , change the index and try diffrent images out

