#!/bin/sh

curl -X POST -d @- -H "Content-Type: application/json" http://127.0.0.1:5002/batch_release << DATA
{
    "batch_id": "B-20210423-00024",
    "product": "RGX-121 BDS0012-01",
    "sample_ids": ["S-210423-00187", "S-210423-00187", "S-210423-00187"],
    "test_methods": ["methodA", "methodB", "methodC"],
    "responses": [7.93, 223, 0.34, 42],
    "model": "RM1",
    "model_parms": ["parm1", "parm2", "parm3"]
}
DATA