Captcha site: http://hqadmin.thm:8000

Start Docker container
```bash
docker run -d -v /tmp/data:/tempdir/ aocr/full
```
Exec into container
```bash
docker exec -it <container_id> bash
```

```bash
cd /ocr/labels
aocr test testing.tfrecords
cd /ocr/ && cp -r model /tempdir/
exit
```
Kill the container
```bash
docker kill <container_id>
```

Run TensorFlow Serving
```bash
docker run -t --rm -p 8501:8501 -v /tmp/data/model/exported-model:/models/ -e MODEL_NAME=ocr tensorflow/serving
```
Available at http://localhost:8501/v1/models/ocr/

Start bruteforcing
```bash
cd Dekstop/bruteforcer
python3 bruteforce.py
```

Result:
admin:ReallyNotGonnaGuessThis


# What key process of training a neural network is taken care of by using a CNN?
feature extraction

# What is the name of the process used in the CNN to extract the features?
convolution

# What is the name of the process used to reduce the features down?
pooling

# What off-the-shelf CNN did we use to train a CAPTCHA-cracking OCR model?
Attention OCR

# What is the password that McGreedy set on the HQ Admin portal?
ReallyNotGonnaGuessThis

# What is the value of the flag that you receive when you successfully authenticate to the HQ Admin portal?
THM{Captcha.Can't.Hold.Me.Back}
