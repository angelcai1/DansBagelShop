document.title = "Menu Editor";
var body = document.querySelector('body');
var br = document.createElement('br');
//header div
var HeaderDiv = document.createElement('div');
HeaderDiv.setAttribute('class', 'black stuff-box shadowed');
var HeaderH1 = document.createElement('h1');
HeaderH1.textContent = "Menu Editor";
HeaderDiv.appendChild(HeaderH1);

//div that prompts user to add a section
var sectionDiv = document.createElement('div');
sectionDiv.setAttribute('class', 'stuff-box shadowed');
var sectionP = document.createElement('p');
sectionP.textContent = "section title";

var sectForm = document.createElement('form');
sectForm.id = 'section';

var sectTitle = document.createElement('input');
sectTitle.type = 'string';

var addButton = document.createElement('button');
addButton.type = 'submit';
addButton.textContent = 'add section';
addButton.addEventListener('click', function(event){
    event.preventDefault();
    var newDiv = document.createElement('div');
    newDiv.setAttribute('class', 'white section-box shadowed');
    // @TODO create a button that removes the most recent section div
    // newDiv.addEventListener('click', function(event){
    //     name_priceDiv.remove();
    // });
    var itemH2 = document.createElement('h2');
    itemH2.textContent = sectTitle.value;

    var itemForm = document.createElement('form');
    itemForm.id = 'item';
    itemForm.action = "/fasdf"
    itemForm.method = "post";
    
    var itemTitle = document.createElement('input');
    itemTitle.type = 'string';
    itemTitle.size = "10"
    itemTitle.maxLength = "12";
    var itemPrice = document.createElement('input');
    itemPrice.type = 'string';
    itemPrice.size = "6";
    
    var addItemButton = document.createElement('button');
    addItemButton.type = 'submit';
    addItemButton.textContent = 'add item';
    addItemButton.addEventListener('click', function(event){
        event.preventDefault();

        name_priceDiv = document.createElement('div');
        name_priceDiv.setAttribute('class', 'align_right')
        var name_priceP = document.createElement('p');
        name_priceP.textContent = itemTitle.value + "__________________________________" + itemPrice.value;
        // @TODO create a button that removes the most recent name_priceDiv
        name_priceDiv.addEventListener('click', function(event){
            name_priceDiv.remove();
        });
        name_priceDiv.append(name_priceP)
        newDiv.appendChild(name_priceDiv);
    });
    itemForm.append("Item name: ",itemTitle , " Price: ",  itemPrice, " ", addItemButton);
    newDiv.append(itemH2, itemForm);
    body.append(newDiv);
});

sectForm.append(sectTitle, addButton)
sectionDiv.append(sectionP, sectForm)
body.append(HeaderDiv, sectionDiv);