var d = document,
    itemBox = d.querySelectorAll('.item_box'), // блок каждого товара
		cartCont = d.getElementById('cart_content'); // блок вывода данных корзины
// Функция кроссбраузерная установка обработчика событий
function addEvent(elem, type, handler){
  if(elem.addEventListener){
    elem.addEventListener(type, handler, false);
  } else {
    elem.attachEvent('on'+type, function(){ handler.call( elem ); });
  }
  return false;
}
// Получаем данные из LocalStorage
function getCartData(){
	return JSON.parse(localStorage.getItem('cart'));
}
// Записываем данные в LocalStorage
function setCartData(o){
	localStorage.setItem('cart', JSON.stringify(o));
	return false;
}
// Добавляем товар в корзину
function addToCart(e){
	this.disabled = true; // блокируем кнопку на время операции с корзиной
	var cartData = getCartData() || {}, // получаем данные корзины или создаём новый объект, если данных еще нет
			parentBox = this.parentNode, // родительский элемент кнопки &quot;Добавить в корзину&quot;
			itemId = this.getAttribute('data-id'), // ID товара
			itemTitle = parentBox.querySelector('.item_title').innerHTML, // название товара
			itemPrice = parentBox.querySelector('.item_price').innerHTML; // стоимость товара
	if(cartData.hasOwnProperty(itemId)){ // если такой товар уже в корзине, то добавляем +1 к его количеству
		cartData[itemId][2] += 1;
	} else { // если товара в корзине еще нет, то добавляем в объект
		cartData[itemId] = [itemTitle, itemPrice, 1];
	}
	// Обновляем данные в LocalStorage
	if(!setCartData(cartData)){
		this.disabled = false; // разблокируем кнопку после обновления LS
		cartCont.innerHTML = 'Product added to cart.';
		setTimeout(function(){
			cartCont.innerHTML = 'Continue shopping...';
		}, 1000);
	}
	return false;
}
// Устанавливаем обработчик события на каждую кнопку &quot;Добавить в корзину&quot;
for(var i = 0; i < itemBox.length; i++){
	addEvent(itemBox[i].querySelector('.add_item'), 'click', addToCart);
}
// Открываем корзину со списком добавленных товаров
function openCart(e){

	var cartData = getCartData(), // вытаскиваем все данные корзины
			totalItems = '';
	console.log(JSON.stringify(cartData));
	// если что-то в корзине уже есть, начинаем формировать данные для вывода
	if(cartData !== null){
		totalItems = '<table class="shopping_list"><tr><th>Name</th><th>Price</th><th>Number</th></tr>';
		var totalCount = 0;
		var totalPrice = 0;
		for (var itemCode in cartData) {
		   var itemData = cartData[itemCode];
		   var itemName = itemData[0];
		   var itemCount = itemData[2];
		   var itemPriceText = itemData[1];
		   var itemPrice = parseFloat(itemPriceText.replace('$',''));
		   var dilivery = 10;
		   totalCount += itemCount;
		   totalPrice += itemCount * itemPrice;
		   var total = totalPrice + dilivery;

		   totalItems += `<tr><td>${itemName}</td><td>${itemPriceText}</td><td>${itemCount}</td></tr>`;
		}
		totalItems += `<tr><td>Subtotal:</td><td>${totalPrice}</td><td>${totalCount}</td><td>+ Dilivery 10$</td><br></tr><tr><td>Total:</td><td>${total}</td></tr>`;
		totalItems += '<table>';
		cartCont.innerHTML = totalItems;
	} else {
		// если в корзине пусто, то сигнализируем об этом
		cartCont.innerHTML = 'The cart is empty!';
	}
	return false;
}
/* Открыть корзину */
addEvent(d.getElementById('checkout'), 'click', openCart);
/* Очистить корзину */
addEvent(d.getElementById('clear_cart'), 'click', function(e){
	localStorage.removeItem('cart');
	cartCont.innerHTML = 'Cart emptied.';
});