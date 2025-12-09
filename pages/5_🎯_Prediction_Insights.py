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
    st.image('imgs/features.png')
    st.write('Satisfaction shows high correlations with flying in Business class which is intuitive as it has spacious seating and many perks in comparison to economy. Not all companies cover the cost for flying Business and many have policies that require economy travel unless a certain flight time is reached usually around 5 hours, that\'s a long flight.')
    st.write('50% of the flights for dissatisfied travelers were around 2 hours or less.  Dissatisfied traveler\'s third quartile reached over 3 hours and the maximum over 12 hours! This might not be as bad for a petite person but a more leggy or broad person may find this unbearable.')
    st.divider()
    col1, col2 = st.columns(2, vertical_alignment='bottom', gap='small')
    col1.image('imgs/tall.png', width=300)
    col2.subheader('Challenge:')
    col2.write('Economy Plus is the solution airlines have in place for this demographic having added 3 to 9 inches of legroom depending on the airline.  How do they cater to this demographic from a supply standpoint and to younger populations that may not have the funds to upgrade at this point in their career?')
    col2.subheader('Solution:')
    col2.write('These airlines already advertise to this demographic on their websites encouraging upgrading at booking or checkin for more leg room or discounts for young travelers. They could go a step further and have signage for these groups in the airport and on the plane where the inflight brochures are stored.  Airlines could add to the flight attendant\'s script for passengers to check the entertainment brochures for their flight that has information for added comfort and discounts.')

with tab2:
    st.title('Business Insights')
    st.subheader('Age Demographic:')
    st.write('69% of travelers in this dataset are flying for business, and the median age of satisfied travelers is 43. Notably, every traveler between ages 21 and 43 is traveling for business across all cabin classes. Among adults aged 44–54, those traveling for business exclusively selected Economy Plus or Business Class, reinforcing the idea that mid-career professionals tend to prioritize comfort, convenience, or loyalty benefits. These age patterns make sense: by their late 30s and 40s, many frequent travelers have accumulated loyalty points or gained corporate status that grants them upgrades or access to premium cabins.')
    st.divider()
    col1, col2,  = st.columns(2, vertical_alignment='center')
    col1.image('imgs/blog.jpg', width=300)
    col1.image('imgs/points.jpg', width=300)
    col2.subheader('Recommendation:')
    col2.divider()
    col2.write('This suggests an opportunity for airlines to enhance satisfaction among newer or younger travelers. For example, airlines could publish an educational blog explaining how to earn and redeem loyalty points effectively.')
    col2.write('They could also highlight partnerships with merchants that allow travelers to accumulate points through everyday spending, helping more customers experience the rewarding aspects of loyalty programs earlier in their travel journey.')
    col2.divider()
    st.divider()
    st.subheader('Inflight Entertainment & WIFI:')
    st.image('imgs/entertainment.jpg')
    st.write('Entertainment experience can be maximized when properly planned.  Airline entertainment databases are extensive and giving customers communication emails to help them plan entertainment before their trip by sending links to their monthly available movies and tv shows could help satisfaction in this metric.')
    st.write('Children aged 7-12 and male minors aged 16-20 rated inflight WIFI as a 2 on a scale from 0-5 on flights a little over 2 hours long.  This young demographic may not be able to comprehend the WIFI requirement in the air and are more accustomed to a certain amount of ongoing usage with unlimited plans on land.')
    st.write('In the airline marketing email sent to the parents or the adults in this demographic could advertise the premium WIFI offering that is capable of high-speed streaming. Emails could nudge parents as using the service to have children save for their travel in order to enjoy their usual online habits.  Likewise, the minors may have some foresight of what to expect and contemplate the purchase prior to the trip.')

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
            st.write('Testing accuracy: 96.2%')
            st.write('🔬 Test Sensitivity: 94.1%')
            st.write('🧪 Precision: 97.0%')
            st.write('Tree depth = unconstrained')
            st.write('Overfits')
        with col2:
            st.subheader('Hyperparameter Tuning')
            st.image('imgs/rf_hyper.png', width=300)
            st.write('Training accuracy: 99.6%')
            st.write('Testing accuracy: 96.4%')
            st.write('🔬 Test Sensitivity: 94.5% ')
            st.write('🧪 Precision: 97.1%')
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
        col1, col2 = st.columns(2, vertical_alignment='top', gap='medium')
        with col1:
            st.subheader('Linear SVC')
            st.divider()
            st.image('imgs/lin_svc.png', width=300)
            st.write('Training accuracy: 87.6%')
            st.write('Testing accuracy: 87.2%')
            st.write('🔬 Test Sensitivity: 83.2%')
            st.write('🧪 Precision: 86.8%')
        with col2:
            st.subheader('RBF SVC')
            st.divider()
            st.image('imgs/rbf_svc.png', width=300)
            st.write('Training accuracy: 95.8%')
            st.write('Testing accuracy: 95.3%')
            st.write('🔬 Test Sensitivity: 93.5% ')
            st.write('🧪 Precision: 95.6%')
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
        st.image('imgs/log_r.png', width=500)
        st.write('Training accuracy: 87.7%')
        st.write('Testing accuracy: 87.3%')
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
        st.image('imgs/test.jpg',width=300)
        st.divider()
        container = st.container(border=True)
        container.write('🌳 The Random Forest model performed the best because the data contains complex, non-linear patterns that linear models miss (Linear SVC & Logistic Regression), and the algorithm is computationally efficient enough to train effectively on a dataset of this size, which challenges the kernel classifier RBF.')
        container.write('The kernel classifier obtained high scores but was extremely slow and computationally expensive since it compares every data point to every other data point taking space of Big O notation of N squared.')
        