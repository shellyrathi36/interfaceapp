const mongoose = require('mongoose');
const express = require('express');
const path = require('path');
const app=express();
const doctor =require('./models/doctor')

app.set('view engine', 'ejs');

app.set('views', path.join(__dirname,'views'));

mongoose.connect('mongodb+srv://shellyrathi37:Sh03082004@cluster0.2zg4kfz.mongodb.net/interfaceapp?retryWrites=true&w=majority',
{
    useNewUrlParser: true,
    useUnifiedTopology: true,

}).then(()=>{
    console.log("connection open !!")
  
})
.catch(err => {
    console.log(err)
})
app.listen(3000, () => {
    console.log("server is running at port 3000")
})
app.get('/', (req, res)=>{
    res.render('medicalpres')
})
app.get('/newpatient', async(req, res)=>{
    const doctors= await doctor.find({})
    res.render('medicalpres',doctors)
})