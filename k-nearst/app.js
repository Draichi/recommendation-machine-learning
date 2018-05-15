var data = import('./lessons.js')

var slct1 = document.getElementById("slct1")
var slct2 = document.getElementById("slct2")

var users = {}

Promise.resolve(data).then(function(value) {
  //console.log(value.default)
  
  for (var i = 0; i < value.default.users.length; i++) {
    name = value.default.users[i].first_name

    var option1 = document.createElement("option")
    var option2 = document.createElement("option")
    option1.value = name
    option2.value = name

    option1.innerHTML = name
    option2.innerHTML = name

    slct1.appendChild(option1)
    slct2.appendChild(option2)

    users[name] = value.default.users[i]
  }
})



var btn = document.getElementById("btn")

btn.addEventListener("click", function () {
  person1 = slct1.value
  person2 = slct2.value

  var keys = Object.keys(users[person1])
  console.log(keys)

  // console.log(users[person1])
  // console.log(users[person2])
})


