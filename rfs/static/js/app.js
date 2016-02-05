/* initialize fluxxor */

var flux = new Fluxxor.Flux();
window.flux = flux;
var FluxMixin = Fluxxor.FluxMixin(React);
var StoreWatchMixin = Fluxxor.StoreWatchMixin;



var product_constants = {
    FETCH_PRODUCT : 'FETCH_PRODUCT'
};

var ProductStore = Fluxxor.createStore({
    
    initialize : function() {
	this.currentProduct = {};
	this.bindActions(
	    product_constants.FETCH_PRODUCT, this.fetchProduct
	);
    },
    
    fetchProduct: function(payload) {
	var that = this;
	jQuery.getJSON(
	    "/api/products/"+payload.productid,
	    function(data) {
		that.currentProduct=data;
		that.emit('change');
	    });	
	//return this.emit('change');
    },
    
    getState : function() {
	return {
	    currentProduct : this.currentProduct
	};
    }
    
});

flux.addStore("ProductStore", new ProductStore());
flux.addAction("fetchProduct", function(productid) {
    this.dispatch(product_constants.FETCH_PRODUCT,{productid : productid});
});

var FluxProduct = React.createClass({displayName: "FluxProduct",
    mixins : [FluxMixin, StoreWatchMixin('ProductStore')],
    getInitialSate : function() {
	return {}
    },
	    
    getStateFromFlux: function() {
	var flux = this.getFlux();
	return flux.store('ProductStore').getState();
    },
    
    componentDidMount: function() {
	this.getFlux().actions.fetchProduct(this.props.productid);
    },
    
    render: function() {
	return (
		React.createElement("h1", {className: "name"}, this.state.currentProduct.title)
	);
    }
});

var cart_constants = {
    //CART_ADD: 'CART_ADD',
    //CART_CHANGE: 'CART_CHANGE',
    //CART_CLEAR: 'CART_CLEAR',
    FETCH_CART : 'FETCH_CART',
};

var CartStore = Fluxxor.createStore({
    
    initialize : function() {
	this.currentCart = {id:0,orderlines:[]};
	this.bindActions(
	    cart_constants.FETCH_CART, this.fetchCart
	);
    },
    
    fetchCart: function(payload) {
	var that = this;
	jQuery.getJSON(
	    "/api/orders/"+payload.cartid,
	    function(data) {
		that.currentCart=data;
		that.emit('change');
	    });	
	//return this.emit('change');
    },
    
    getState : function() {
	return {	    
	    currentCart : this.currentCart
	};
    }
    
});

flux.addStore("CartStore", new CartStore());
flux.addAction("fetchCart", function(cartid) {
    this.dispatch(cart_constants.FETCH_CART,{cartid : cartid});
});

var ListItemWrapper = React.createClass({displayName: "ListItemWrapper",
    render: function() {
	return (React.createElement("li", null, "CartLine ", this.props.data.extradata, " ", this.props.data.quantity, " x € ", this.props.data.unit_price));
    }
});

var FluxCart = React.createClass({displayName: "FluxCart",
    mixins : [FluxMixin, StoreWatchMixin('CartStore')],
    getInitialSate : function() {
	return {currentCart:{id:0,
			     orderlines:[]}

	       }
    },
	    
    getStateFromFlux: function() {
	var flux = this.getFlux();
	return flux.store('CartStore').getState();
    },
    
    componentDidMount: function() {
	this.getFlux().actions.fetchCart(this.props.cartid);
    },
    
    render: function() {
	return (React.createElement("div", {class: "cart"}, 
		React.createElement("h1", {className: "name"}, "Cart ", this.state.currentCart.id), 
				React.createElement("ul", null, 
		this.state.currentCart.orderlines.map(function(orderline) {
		    return React.createElement(ListItemWrapper, {key: orderline.id, data: orderline});
		})
		)

		)
	);
    }
});

React.render(
	React.createElement(FluxProduct, {flux: flux, productid: "1"}),
    document.getElementById('flux-product')    
);
React.render(
	React.createElement(FluxCart, {flux: flux, cartid: "1"}),
    document.getElementById('flux-cart')    
);
