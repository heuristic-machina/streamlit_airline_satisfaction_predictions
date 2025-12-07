import streamlit as st

#tabs
st.title('Insights and Conclusion')
tab1, tab2, tab3 = st.tabs(['Top Factors', 'Business Insights', 'Experimental Findings'])

with tab1:
    st.header('✈️ Top Factors')
    st.markdown("""
The most influential important factors in predicting airline satisfaction are:
 - Online Boarding
 - Inflight Wifi
 - Type of Travel
 - Business Class
 - Inflight Entertainment    
""")
    st.image('imgs/features.png', caption="Important Factors")
    st.write('Satisfaction shows high correlations with business travelers and the services aligned with on board technologies.  This is logical as business travelers would manage the flight down time to knock out some work related projects or to look over presentation notes.')

with tab2:
    st.subheader('Business Insights')
    st.write('Business travelers generally know how businesses work, so they\'re more likely to fill out surveys than the average passenger. That familiarity with the system also tends to make them more appreciative and therefore more satisfied with the service.')
    st.write('62\% of the airline\'s customers are loyal and 100\% of them are business travelers.  Interestingly the disloyal customers, guess what are also traveling for business and make up a whopping 99\%.')
    st.write('So how can this be?  Shouldn\'t we see more positive satisfaction?  We should if we know for sure these travelers are not just upgrading to business for better amenities and so the actual metric is not reflected as the actual business person but perhaps some entitled type instead.  So the issue is not the service.  It\'s the inflated sense of deservedness.  Or there are others who don\'t see the value in feedback and this a key group to target.')
    st.write('The airline should emphasize survey participation makes a difference for improvements their valued customers can make through their feedback, good or bad.  The surveys should be easily accessible through email or qr code and have a segment for the customers to add their feedback. Survey Monkey supplied a pro tip that people are more inclined to complete surveys on Thursdays and Fridays between 7am and 1pm PST, so sending out survey requests during peak response times may increase participation.')

with tab3:
    tab1, tab2, tab3, tab4 = st.tabs(['Random Forest', 'SVC', 'Logistic Regression', 'Test Summary'])
    with tab1:
        st.header('🌳 Random Forest Classifier:')
        st.divider()
        col1, col2 = st.columns(2, vertical_alignment='top', gap='large')
        with col1:
            st.subheader('Default')
            st.image('imgs/rf.png', width=300)
            st.write('Training accuracy: 100%')
            st.write('Testing accuracy: 96.2\%')
            st.write('🔬 Test Sensitivity: 94.1\%')
            st.write('🧪 Precision: 97.0\%')
            st.write('Tree depth = unconstrained')
            st.write('Overfits')
        with col2:
            st.subheader('Hyperparameter Tuning')
            st.image('imgs/rf_hyper.png', width=300)
            st.write('Training accuracy: 99.6\%')
            st.write('Testing accuracy: 96.4\%')
            st.write('🔬 Test Sensitivity: 94.5\% ')
            st.write('🧪 Precision: 97.1\%')
            st.write('Tree depth = 20')
            st.write('Training = Generalized')
            st.write('Max Features = 0.5')
            st.write('Estimators = 100')
        st.divider()
        st.header('Hyperparameter Tuning Closer Look:')
        container = st.container(border=True)
        container.write('1. Limiting the depths of trees helps better generalization instead of memorizing the training set')
        container.write('2. The maximum number of features considered when looking for splits at the nodes introduces more randomness reducing overfitting')
        container.write('3. Greater number of estimators generally lead to better performance but increase computational costs')

    with tab2:
        st.image('imgs/scatter.jpg', width=100)
        st.header('Support Vector Classifier:')
        st.write('Regularization: C = 1')
        st.divider()
        col1, col2 = st.columns(2, vertical_alignment='top', gap='large')
        with col1:
            st.subheader('Linear SVC')
            st.divider()
            st.image('imgs/lin_svc.png', width=300)
            st.write('Training accuracy: 87.6\%')
            st.write('Testing accuracy: 87.2\%')
            st.write('🔬 Test Sensitivity: 83.2\%')
            st.write('🧪 Precision: 86.8\%')
        with col2:
            st.subheader('RBF SVC')
            st.divider()
            st.image('imgs/rbf_svc.png', width=300)
            st.write('Training accuracy: 95.8\%')
            st.write('Testing accuracy: 95.3\%')
            st.write('🔬 Test Sensitivity: 93.5% ')
            st.write('🧪 Precision: 95.6\%')
            st.write('Gamma = Scale')
            st.latex(r'''
                gamma = \left(\frac{1}{n features * variance(X)}\right)
            ''')    
        st.divider()
        st.header('SVC Closer Look:')
        container = st.container(border=True)
        container.write('1. In both SVC models C acts as a penalty parameter for errors and controls optimization')
        container.write('2. Small C gives higher bias and lower variance with a larger margin and large C gives lower bias and higher variation with narrower margin.')
        container.markdown("""
3. RBF\'s kernel coefficient gamma determines the radius of influence:
 - Small gamma examines data points far away in radius to determine the separation line
 - Large gamma examines data points very close data points in the decision boundary and is can be complex and prone to overfitting   
""")


    with tab3:
        st.image('imgs/log.png', width=100)
        st.header('Logistic Regression')
        st.divider()
        st.image('imgs/log_r.png', width=300)
        st.write('Training accuracy: 87.7\%')
        st.write('Testing accuracy: 87.3\%')
        st.write('🔬 Test Sensitivity: 83.4%')
        st.write('🧪 Precision: 86.8%')
        st.divider()
        st.header('Logistic Regression Closer Look:')
        container = st.container(border=True)
        container.write('Logistic Regression estimates the probability that a given data point belongs to a certain class by using the sigmoid function:')
        container.latex(r'''
                P(X) = \left(\frac{1}{1 + e^-(\beta_0+\beta_1X_1+...+\beta_kX_k) }\right)
            ''')
        container.write('The probability is then used to calculate the class label from a threshold:')
        container.latex(r'''
                P(X) \geq 0.5\text{, classify as Class 1 (Yes)}                                              
            ''')
        container.latex(r'''                     
                P(X) \lt 0.5\text{, classify as Class 0 (No)}                        
            ''')
        st.write('Logistic regression is highly efficient making it a good baseline model')

    with tab4:
        st.header('Model Test Summary')
        st.image('imgs/test.jpg', width=300)
        st.divider()
        container = st.container(border=True)
        container.write('🌳 The Random Forest model performed the best because the data contains complex, non-linear patterns that linear models miss (Linear SVC & Logistic Regression), and the algorithm is computationally efficient enough to train effectively on a dataset of this size, which challenges the kernel classifier RBF.')
        container.write('The kernel classifier obtained high scores but was extremely slow and computationally expensive since it compares every data point to every other data point taking space of Big O notation of N squared.')
        