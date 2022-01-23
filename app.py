from flask import Flask, render_template, request
import pandas as pd
import joblib

app= Flask(__name__)

# Rendering the welcome page from where the 
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        data_dict = {
        'Product_Info_1':[float(request.form['product_info_1'])],
        'Product_Info_2':[request.form.get('product_info_2')],
        'Product_Info_3':[float(request.form['product_info_3'])],
        'Product_Info_4':[float(request.form['product_info_4'])], 
        'Product_Info_5':[float(request.form['product_info_5'])],
        'Product_Info_6':[float(request.form['product_info_6'])],
        'Product_Info_7':[float(request.form['product_info_7'])],
        'Ins_Age':[float(request.form['ins_age'])], 
        'Ht':[float(request.form['ht'])], 'Wt':[float(request.form['wt'])],
        'BMI':[float(request.form['bmi'])],
        'Employment_Info_1':[float(request.form['employment_info_1'])],
        'Employment_Info_2':[float(request.form['employment_info_2'])],
        'Employment_Info_3':[float(request.form['employment_info_3'])],
        'Employment_Info_4':[float(request.form['employment_info_4'])],
        'Employment_Info_5':[float(request.form['employment_info_5'])],
        'Employment_Info_6':[float(request.form['employment_info_6'])],
        'InsuredInfo_1':[float(request.form['insuredInfo_1'])],
        'InsuredInfo_2':[float(request.form['insuredInfo_2'])],
        'InsuredInfo_3':[float(request.form['insuredInfo_3'])],
        'InsuredInfo_4':[float(request.form['insuredInfo_4'])],
        'InsuredInfo_5':[float(request.form['insuredInfo_5'])],
        'InsuredInfo_6':[float(request.form['insuredInfo_6'])],
        'InsuredInfo_7':[float(request.form['insuredInfo_7'])],
        'Insurance_History_1':[float(request.form['insurance_history_1'])],
        'Insurance_History_2':[float(request.form['insurance_history_2'])],
        'Insurance_History_3':[float(request.form['insurance_history_3'])],
        'Insurance_History_4':[float(request.form['insurance_history_4'])],
        'Insurance_History_5':[float(request.form['insurance_history_5'])],
        'Insurance_History_6':[float(request.form['insurance_history_6'])],
        'Insurance_History_7':[float(request.form['insurance_history_7'])],
        'Insurance_History_8':[float(request.form['insurance_history_8'])],
        'Insurance_History_9':[float(request.form['insurance_history_9'])],
        'Family_Hist_1':[float(request.form['family_hist_1'])],
        'Family_Hist_2':[float(request.form['family_hist_2'])],
        'Family_Hist_3':[float(request.form['family_hist_3'])],
        'Family_Hist_4':[float(request.form['family_hist_4'])],
        'Family_Hist_5':[float(request.form['family_hist_5'])],
        'Medical_History_1':[float(request.form['medical_history_1'])],
        'Medical_History_2':[float(request.form['medical_history_2'])],
        'Medical_History_3':[float(request.form['medical_history_3'])],
        'Medical_History_4':[float(request.form['medical_history_4'])],
        'Medical_History_5':[float(request.form['medical_history_5'])],
        'Medical_History_6':[float(request.form['medical_history_6'])],
        'Medical_History_7':[float(request.form['medical_history_7'])],
        'Medical_History_8':[float(request.form['medical_history_8'])],
        'Medical_History_9':[float(request.form['medical_history_9'])],
        'Medical_History_10':[float(request.form['medical_history_10'])],
        'Medical_History_11':[float(request.form['medical_history_11'])],
        'Medical_History_12':[float(request.form['medical_history_12'])],
        'Medical_History_13':[float(request.form['medical_history_13'])],
        'Medical_History_14':[float(request.form['medical_history_14'])],
        'Medical_History_15':[float(request.form['medical_history_15'])],
        'Medical_History_16':[float(request.form['medical_history_16'])],
        'Medical_History_17':[float(request.form['medical_history_17'])],
        'Medical_History_18':[float(request.form['medical_history_18'])],
        'Medical_History_19':[float(request.form['medical_history_19'])],
        'Medical_History_20':[float(request.form['medical_history_20'])],
        'Medical_History_21':[float(request.form['medical_history_21'])],
        'Medical_History_22':[float(request.form['medical_history_22'])],
        'Medical_History_23':[float(request.form['medical_history_23'])],
        'Medical_History_24':[float(request.form['medical_history_24'])],
        'Medical_History_25':[float(request.form['medical_history_25'])],
        'Medical_History_26':[float(request.form['medical_history_26'])],
        'Medical_History_27':[float(request.form['medical_history_27'])],
        'Medical_History_28':[float(request.form['medical_history_28'])],
        'Medical_History_29':[float(request.form['medical_history_29'])],
        'Medical_History_30':[float(request.form['medical_history_30'])],
        'Medical_History_31':[float(request.form['medical_history_31'])],
        'Medical_History_32':[float(request.form['medical_history_32'])],
        'Medical_History_33':[float(request.form['medical_history_33'])],
        'Medical_History_34':[float(request.form['medical_history_34'])],
        'Medical_History_35':[float(request.form['medical_history_35'])],
        'Medical_History_36':[float(request.form['medical_history_36'])],
        'Medical_History_37':[float(request.form['medical_history_37'])],
        'Medical_History_38':[float(request.form['medical_history_38'])],
        'Medical_History_39':[float(request.form['medical_history_39'])],
        'Medical_History_40':[float(request.form['medical_history_40'])],
        'Medical_History_41':[float(request.form['medical_history_41'])],
        'Medical_Keyword_1':[float(request.form['medical_keyword_1'])],
        'Medical_Keyword_2':[float(request.form['medical_keyword_2'])],
        'Medical_Keyword_3':[float(request.form['medical_keyword_3'])],
        'Medical_Keyword_4':[float(request.form['medical_keyword_4'])],
        'Medical_Keyword_5':[float(request.form['medical_keyword_5'])],
        'Medical_Keyword_6':[float(request.form['medical_keyword_6'])],
        'Medical_Keyword_7':[float(request.form['medical_keyword_7'])],
        'Medical_Keyword_8':[float(request.form['medical_keyword_8'])],
        'Medical_Keyword_9':[float(request.form['medical_keyword_9'])],
        'Medical_Keyword_10':[float(request.form['medical_keyword_10'])],
        'Medical_Keyword_11':[float(request.form['medical_keyword_11'])],
        'Medical_Keyword_12':[float(request.form['medical_keyword_12'])],
        'Medical_Keyword_13':[float(request.form['medical_keyword_13'])],
        'Medical_Keyword_14':[float(request.form['medical_keyword_14'])],
        'Medical_Keyword_15':[float(request.form['medical_keyword_15'])],
        'Medical_Keyword_16':[float(request.form['medical_keyword_16'])],
        'Medical_Keyword_17':[float(request.form['medical_keyword_17'])],
        'Medical_Keyword_18':[float(request.form['medical_keyword_18'])],
        'Medical_Keyword_19':[float(request.form['medical_keyword_19'])],
        'Medical_Keyword_20':[float(request.form['medical_keyword_20'])],
        'Medical_Keyword_21':[float(request.form['medical_keyword_21'])],
        'Medical_Keyword_22':[float(request.form['medical_keyword_22'])],
        'Medical_Keyword_23':[float(request.form['medical_keyword_23'])],
        'Medical_Keyword_24':[float(request.form['medical_keyword_24'])],
        'Medical_Keyword_25':[float(request.form['medical_keyword_25'])],
        'Medical_Keyword_26':[float(request.form['medical_keyword_26'])],
        'Medical_Keyword_27':[float(request.form['medical_keyword_27'])],
        'Medical_Keyword_28':[float(request.form['medical_keyword_28'])],
        'Medical_Keyword_29':[float(request.form['medical_keyword_29'])],
        'Medical_Keyword_30':[float(request.form['medical_keyword_30'])],
        'Medical_Keyword_31':[float(request.form['medical_keyword_31'])],
        'Medical_Keyword_32':[float(request.form['medical_keyword_32'])],
        'Medical_Keyword_33':[float(request.form['medical_keyword_33'])],
        'Medical_Keyword_34':[float(request.form['medical_keyword_34'])],
        'Medical_Keyword_35':[float(request.form['medical_keyword_35'])],
        'Medical_Keyword_36':[float(request.form['medical_keyword_36'])],
        'Medical_Keyword_37':[float(request.form['medical_keyword_37'])],
        'Medical_Keyword_38':[float(request.form['medical_keyword_38'])],
        'Medical_Keyword_39':[float(request.form['medical_keyword_39'])],
        'Medical_Keyword_40':[float(request.form['medical_keyword_40'])],
        'Medical_Keyword_41':[float(request.form['medical_keyword_41'])],
        'Medical_Keyword_42':[float(request.form['medical_keyword_42'])],
        'Medical_Keyword_43':[float(request.form['medical_keyword_43'])],
        'Medical_Keyword_44':[float(request.form['medical_keyword_44'])],
        'Medical_Keyword_45':[float(request.form['medical_keyword_45'])],
        'Medical_Keyword_46':[float(request.form['medical_keyword_46'])],
        'Medical_Keyword_47':[float(request.form['medical_keyword_47'])],
        'Medical_Keyword_48':[float(request.form['medical_keyword_48'])]
    }
        data= pd.DataFrame(data_dict)

        file= joblib.load('final_model.joblib')
        
        model= file['model']
        numeric_cols= file['numeric_cols']
        categorical_cols= file['categorical_cols']
        encoded_cols= file['encoded_cols']
        imputer= file['imputer']
        encoder= file['encoder']
        scaler= file['scaler']

        data[numeric_cols]= imputer.transform(data[numeric_cols])
        data[encoded_cols]= encoder.transform(data[categorical_cols])
        data[numeric_cols]= scaler.transform(data[numeric_cols])
        X_input= data[numeric_cols + encoded_cols]
        preds= model.predict(X_input)

        return render_template('result.html', preds=preds[0])
        
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()