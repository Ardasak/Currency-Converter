class styles():
    specific_button_style = """QPushButton{
        background-color: #ADE9E9;
        border: 1px solid #ADE9E9;
        border-radius: 20px;
        width: 120px;
        height: 40px;
        margin-top: 10px;
    }
    QPushButton:hover{
        background-color: #ADD8E6;
    }
    """
    result_textview_style = """QLabel{
        color: white;
    }"""
    currency_combobox_style = """QComboBox{
            height: 75px;
            width: 350px;
            background: gray;
            border: white 5px solid;
            border-radius: 15px;
            color: black;
    }
    QComboBox::drop-down{
        border: white 5px solid;
        border-radius: 15px;
    }
    QComboBox::down-arrow{
        
        image:url(:/down-arrow.png);
        padding-right:5px;
    }

    """

    amount_edittext_style = """QLineEdit{
            background: white;
            color: black;
            border-style: solid;
            border-width: 3px;
            padding: 5px;
            border-color:black;
            border-radius: 15px;
            height: 25px;
        }
        
        QLineEdit:focus{
            
        }
        
    """
    calculate_button_style = """QPushButton{
            background: white;
            color: black;
    }
    """