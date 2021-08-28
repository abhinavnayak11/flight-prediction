function fn1()
{   
    var source = document.getElementById('source').value;
    // alert(source)
    if (source == "Banglore"){
      document.getElementById('destination').innerHTML = "<option value=''>--select one--</option><option value='Cochin'>Cochin</option> <option value='Delhi'>Delhi</option> <option value='New Delhi'>New Delhi</option> <option value='Hyderabad'>Hyderabad</option> <option value='Kolkata'>Kolkata</option>"
    } 
    else if (source == "Delhi"){
      document.getElementById('destination').innerHTML = "<option value=''>--select one--</option><option value='Banglore'>Bangalore</option> <option value='Cochin'>Cochin</option> <option value='New Delhi'>New Delhi</option> <option value='Hyderabad'>Hyderabad</option> <option value='Kolkata'>Kolkata</option>"
    } 
    else if (source == "Kolkata"){
      document.getElementById('destination').innerHTML = "<option value=''>--select one--</option><option value='Banglore'>Bangalore</option> <option value='Cochin'>Cochin</option> <option value='Delhi'>Delhi</option> <option value='New Delhi'>New Delhi</option> <option value='Hyderabad'>Hyderabad</option>"
    } 
    else if (source == "item0"){
      document.getElementById('destination').innerHTML = "<option value=''>--select from first--</option>"
    }
    else {
      document.getElementById('destination').innerHTML = "<option value=''>--select one--</option><option value='Banglore'>Bangalore</option><option value='Cochin'>Cochin</option><option value='Delhi'>Delhi</option><option value='New Delhi'>New Delhi</option><option value='Hyderabad'>Hyderabad</option><option value='Kolkata'>Kolkata</option>"
    }
}

var today = new Date().toISOString().split('T')[0];
document.getElementsByName("dep_date")[0].setAttribute('min', today);
