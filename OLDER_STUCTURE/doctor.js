const mongoose =require('mongoose');

const doctorschema= new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    specialty:{
        type:String,
        required: true
    }
})
const Doctor= mongoose.model('doctordata', doctorschema)
module.exports=Doctor