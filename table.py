test = {
    "table_7c5e398b4c894e66aab4b7e02f697521": [
        [
            "Lab Code",
            ":CPC-AP-113"
        ],
        [
            "Sample Drawn Date",
            ":2022-04-26 09:22"
        ],
        [
            "Registration Date",
            "2022-04-26 09:23"
        ],
        [
            "Approved Date",
            ":2022-04-26 09:56"
        ]
    ],
    "table_65b8b4440c4c4dcd8ccdc7440912e7bb": [
        [
            "Sample ID",
            ":1524952 NaF Fasting"
        ],
        [
            "Patient ID",
            ":641523"
        ],
        [
            "Ref. Doctor :",
            " "
        ],
        [
            "Ref. Customer :",
            " "
        ]
    ],
    "table_38887c7a36b0430e8b9cd820ae99d6aa": [
        [
            "CLINICAL",
            "BIOCHEMISTRY",
            " ",
            " "
        ],
        [
            "Test Description",
            "Result",
            "Units",
            "Biological Reference Ranges"
        ],
        [
            "Glucose-Fasting (FBS) (Method Spectrophotometry)",
            "198",
            "mg/dL",
            "70 100 Normal 100 126 Pre Diabetic > 126 Diabetic"
        ]
    ]
}

def print_table(data):
            for key, values in data.items():
                print("\n")
                for value in values:
                    row = "|".join([str(x).ljust(20) for x in value])
                    print(row)
                    
print_table(test)