import streamlit as st
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
 
import pandas as pd

# Loading the data
df = pd.read_csv('mushrooms.csv')
# Cleaning the data

for col in df.columns:
    df[col] = df[col].astype("category")
    df[col] = df[col].cat.codes

# Modelling
X = df.drop("class", axis=1)
y = df["class"]
# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Creating and training the model
decision_model = DecisionTreeClassifier()
decision_model.fit(X_train, y_train)
y_pred = decision_model.predict(X_test)


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

cap_shapelst = ['bell','conical','flat','knobbed','sunken','convex']
cap_surfacelst = ['fibrous','grooves','smooth','scaly']
capcolor_lst = ['buff','cinnamon','red','gray','brown','pink','purple','green','white','yellow' ]
bruises_lst = ['Not bruised','bruised']
Odor_lst = ['almond','creosote','foul','anise','musty','none','pungent','spicy','fishy']
gillattachment_lst = ['attached','descending','free','notched']
gillspacing_lst = ['closed','distant','crowded']
gillsize_lst = ['broad','narrow']
gillcolor_lst = ['buff','red','gray','chocolate','black','brown','orange','pink','green','purple','white','yellow'] 
stalkshape_lst = ['enlarging','tapering']
stalkroot_lst = ['missing','bulbous','club','equal','rooted','cup','rhizomorphs']
stalksurfaceabovering_lst = ['fibrous','silky','smooth','scaly']
stalkerbelowring_lst = ['fibrous','silky','smooth','scaly']
stalkcolorabovering_lst = ['buff','cinnamon','red','gray','brown','orange','pink','white','yellow']
stalkcolorbelowring_lst = ['buff','cinnamon','red','gray','brown','orange','pink','white','yellow']
veiltype_lst = ['partial','universal']
veilcolor_lst = ['brown','orange','white','yellow']
ringnumber_lst = ['none','one','two']
ringtype_lst = ['cobwebby','evanescent','flaring','large','none','pendent','sheathing','zone']
sporeprintcolor_lst = ['buff','chocolate','black','brown','orange','green','purple','white','yellow']
population_lst = ['abundant','clustered','numerous','scattered','several','solitary']
habitat_lst = ['woods','grasses','leaves','meadows','paths','urban','waste']
#Put in sidebars

app_modes = st.sidebar.selectbox("SELECT PAGE:",['Home page','Prediction'])

#HOME PAGE FIRST
if app_modes == "Home page":
    st.markdown("<h1 style = 'font-family:courier;'>EDIBLE😋 or DEADIBLE☠️</h1>", unsafe_allow_html=True)
    col1, col2= st.columns(2)
    with col1:    
        st.markdown("<h2 style = 'font-family:courier;'>Welcome To EoD</h2>", unsafe_allow_html=True)
        st.write("An app used to tell you whether the mushroom you have is yummy or can send you straight to the ICU")
    with col2:
        st.subheader("How it works:")
        st.write("""
                 1.\t Select the prediction page on the side bar \n
                 2.\t Fill in all the features required according to what you can observe from your mushroom \n
                 3.\t Press the '😋 / ☠️ ' button to get your result \n
                 4.\t Enjoy your mushroom! 😁
                  """)
    #WE WILL ADD SOME INFO HERE.
elif app_modes == "Prediction":
    st.title("EoD")
    st.subheader('We will use this information to know the mushroom.')
    st.header("Features of the mushroom")
    
    # Put radio buttons
    cap_shape = st.selectbox('Cap Shape',cap_shapelst)
    cap_surface = st.selectbox('Cap surface',cap_surfacelst)
    capcolor = st.selectbox('Cap color',capcolor_lst)
    bruises = st.selectbox("Bruises",bruises_lst)
    Odor = st.selectbox('Odor',Odor_lst)
    gillattachment = st.selectbox("Gill Attachment",gillattachment_lst)
    gillspacing = st.selectbox("Gill Spacing",gillspacing_lst)
    gillsize = st.selectbox("Gill Size",gillsize_lst)
    gillcolor = st.selectbox("Gill Color",gillcolor_lst)
    stalkshape = st.selectbox("Stalk Shape",stalkshape_lst)
    stalkroot = st.selectbox("Stalk Root",stalkroot_lst)
    stalksurfaceabovering= st.selectbox("Stalk Surface Above Ring",stalksurfaceabovering_lst)
    stalkerbelowring = st.selectbox("Stalk Surface Below Ring",stalkerbelowring_lst)
    stalkcolorabovering = st.selectbox("Stalk Color Above Ring",stalkcolorabovering_lst)
    stalkcolorbelowring = st.selectbox("Stalk Color Below Ring",stalkcolorbelowring_lst)
    veiltype = st.selectbox("Veil Type",veiltype_lst)
    veilcolor = st.selectbox("Veil Colour", veilcolor_lst)
    ringnumber = st.selectbox("Ring Number", ringnumber_lst)
    ringtype = st.selectbox("Ring type", ringtype_lst)
    sporeprintcolor = st.selectbox("Spore print color", sporeprintcolor_lst)
    population = st.selectbox("Population", population_lst)
    habitat = st.selectbox("Habitat", habitat_lst)

    pred_button = st.button("😋 / ☠️")
    if (pred_button):
        i1 = int(cap_shapelst.index(cap_shape))
        i2 = int(cap_surfacelst.index(cap_surface))
        i3 = int(capcolor_lst.index(capcolor))
        i4 = int(bruises_lst.index(bruises))
        i5 = int(Odor_lst.index(Odor))
        i6 = int(gillattachment_lst.index(gillattachment))
        i7 = int(gillspacing_lst.index(gillspacing))
        i8 = int(gillsize_lst.index(gillsize))
        i9 = int(gillcolor_lst.index(gillcolor))
        i10 = int(stalkshape_lst.index(stalkshape))
        i11 = int(stalkroot_lst.index(stalkroot))
        i12 = int(stalksurfaceabovering_lst.index(stalksurfaceabovering))
        i13 = int(stalkerbelowring_lst.index(stalkerbelowring))
        i14 = int(stalkcolorabovering_lst.index(stalkcolorabovering))
        i15 = int(stalkcolorbelowring_lst.index(stalkcolorbelowring))
        i16 = int(veiltype_lst.index(veiltype))
        i17 = int(veilcolor_lst.index(veilcolor))
        i18 = int(ringnumber_lst.index(ringnumber))
        i19 = int(ringtype_lst.index(ringtype))
        i20 = int(sporeprintcolor_lst.index(sporeprintcolor))
        i21 = int(population_lst.index(population))
        i22 = int(habitat_lst.index(habitat))

        X = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22]
        edibility = decision_model.predict([X])[0]
        if int(edibility) == 1:
            st.error("The mushroom is poisonous☠️")
        elif int(edibility) == 0:
            st.success("The mushroom is edible😋")