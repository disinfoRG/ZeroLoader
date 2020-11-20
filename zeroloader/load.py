import itertools
import os
import pathlib
import zipfile

import pandas as pd

# self defined functions
from drive import GoogleDrive


def unzip(zip_file):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(os.path.dirname(zip_file))
        os.remove(zip_file)


def get_producer_month_id(producer, month):
    if producer == 'news.ltn.com.tw' and month == '2020-11':
        return "1Dx0k7qEloSxyqVQQSuFyLMkMfNSU22aS"
    # folder_id = ""
    # return folder_id


def load_data(producer, month, data_dir, download=True, service_file='service.json'):
    """
    works with one month only
    """
    if download:
        gdrive = GoogleDrive(service_file)
        item_id = get_producer_month_id(producer, month)
        print(item_id)
        dest_dir = f'/tmp/0archive/{producer}/{month}'
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        unzip(gdrive.download(id=item_id, output_dir=dest_dir))
        data_dir = pathlib.Path(dest_dir)
    # else:
    #     data_dir = pathlib.Path(data_dir)

    df_all = pd.concat([
        pd.read_json(json_file, lines=True, encoding="utf-8")
        for json_file in data_dir.glob(f"{month}-*.jsonl")
    ], ignore_index=True)
    # take the lastest version of each publication in the dataset
    return df_all.sort_values("version").groupby("id").last()
