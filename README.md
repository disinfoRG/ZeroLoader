ZeroLoader
==

A piece of code to read 0archive's public data from [gdrive](https://drive.google.com/drive/u/1/folders/1ckDs03tdXhLdeF0N2St5OP0EeqxFC1bm)

1. Get google api credentials

    Follow Step 1 from [this tutorial](https://developers.google.com/drive/api/v3/quickstart/python).

2. Install the package
3. Create environment file

```shell script
touch .env
echo GDRIVE_PUBLIC_FILE_MAPPING_ID=1OwAGYg7dJob_VMW8vt2FP4fO5Ie7B3EW > .env
```

4. Run

```python
import zeroloader as zl
# 
# df = zl.load.load_data({producer_id}, {yyyy-mm}, {path-to-gdrive-api-credentials})
# e.g. 
# 2020 June's data for storm.mg
df = zl.load_data("5030bba7-81fe-11ea-8627-f23c92e71bad", "2020-06", 'service.json') 
```