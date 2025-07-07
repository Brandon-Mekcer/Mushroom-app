import streamlit as st
import pandas as pd
from model import decision_model
cap_shapelst = ['bell','conical','convex','flat','knobbed','sunken']
cap_surfacelst = ['fibrous','grooves','scaly','smooth']
capcolor_lst = ['brown','buff','cinnamon','gray','green','pink','purple','red','white','yellow']
bruises_lst = ['Has bruises','Does not have bruises']
Odor_lst = ['almond','anice','creosote','fishy','foul','musty','none','pungent','spicy']
gillattachment_lst = ['attached','descending','free','notched']
gillspacing_lst = ['closed','crowded','distant']
gillsize_lst = ['broad','narrow']
gillcolor_lst = ['black','brown','buff','chocolate','gray','green','orange','pink','purple','red','white','yellow']
stalkshape_lst = ['enlarging','tapering']
stalkroot_lst = ['bulbous','club','cup','equal','rhizomorphs','rooted','missing']
stalksurfaceabovering_lst = ['fibrous','scaly','silky','smooth']
stalkerbelowring_lst = ['fibrous','scaly','silky','smooth']
stalkcolorabovering_lst = ['brown','buff','cinnamon','gray','orange','pink','red','white','yellow']
stalkcolorbelowring_lst = ['brown','buff','cinnammon','gray','orange','pink','red','white','yellow']
veiltype_lst = ['partial','universa;']
veilcolor_lst = ['brown','orange','white','yellow']
ringnumber_lst = ['none','one','two']
ringtype_lst = ['cobwebby','evanescent','flaring','large','none','pendent','sheathing','zone']
sporeprintcolor_lst = ['black','brown','buff','chocolate','green','orange','purple','white','yellow']
population_lst = ['abundant','clustered','numerous','scattered','several','solitary']
habitat_lst = ['grasses','leaves','meadows','paths','urban','waste','woods']
#Put in sidebars
app_modes = st.sidebar.selectbox("SELECT PAGE:",['Home page','Prediction'])
#HOME PAGE FIRST
if app_modes == "Home page":
    st.title("KNOW THE MUSHROOM")
    st.image("mushroomimage.jpg")
    st.write('Welcome to the mushroom app. Here is the dataset.')
    data = pd.read_csv('mushrooms.csv')
    st.write(data)
    #WE WILL ADD SOME INFO HERE.
elif app_modes == "Prediction":
    st.subheader('We will use this information to know the mushroom.')
    st.sidebar.header("Features of the mushroom")
    mushroom_type = st.sidebar.text_input("Enter mushroom type:")
    if mushroom_type:
        st.write("The mushroom is: ", mushroom_type)
    # Put radio buttons
    cap_shape = st.sidebar.selectbox('Cap Shape',cap_shapelst)
    cap_surface = st.sidebar.selectbox('Cap surface',cap_surfacelst)
    capcolor = st.sidebar.selectbox('Cap color',capcolor_lst)
    bruises = st.sidebar.selectbox("Bruises",bruises_lst)
    Odor = st.sidebar.selectbox('Odor',Odor_lst)
    gillattachment = st.sidebar.selectbox("Gill Attachment",gillattachment_lst)
    gillspacing = st.sidebar.selectbox("Gill Spacing",gillspacing_lst)
    gillsize = st.sidebar.selectbox("Gill Size",gillsize_lst)
    gillcolor = st.sidebar.selectbox("Gill Color",gillcolor_lst)
    stalkshape = st.sidebar.selectbox("Stalk Shape",stalkshape_lst)
    stalkroot = st.sidebar.selectbox("Stalk Root",stalkroot_lst)
    stalksurfaceabovering= st.sidebar.selectbox("Stalk Surface Above Ring",stalksurfaceabovering_lst)
    stalkerbelowring = st.sidebar.selectbox("Stalk Surface Below Ring",stalkerbelowring_lst)
    stalkcolorabovering = st.sidebar.selectbox("Stalk Color Above Ring",stalkcolorabovering_lst)
    stalkcolorbelowring = st.sidebar.selectbox("Stalk Color Below Ring",stalkcolorbelowring_lst)
    veiltype = st.sidebar.selectbox("Veil Type",veiltype_lst)
    veilcolor = st.sidebar.selectbox("Veil Colour", veilcolor_lst)
    ringnumber = st.sidebar.selectbox("Ring Number", ringnumber_lst)
    ringtype = st.sidebar.selectbox("Ring type", ringtype_lst)
    sporeprintcolor = st.sidebar.selectbox("Spore print color", sporeprintcolor_lst)
    population = st.sidebar.selectbox("Population", population_lst)
    habitat = st.sidebar.selectbox("Habitat", habitat_lst)

    pred_button = st.button("Poisonous/Edible?")
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
        i12 = int(stalksurfaceabovering.index(stalksurfaceabovering))
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
        edibility = decision_model.predict([X])

        if edibility == 1:
            st.text("The mushroom is poisonous")
        elif edibility == 0:
            st.text("The mushroom is edible.")
        