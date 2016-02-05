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

var ListItemWrapper = React.createClass({
    render: function() {
	return (<li>CartLine {this.props.data.extradata} {this.props.data.quantity} x € {this.props.data.unit_price}</li>);
    }
});

var FluxCart = React.createClass({
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
	return (<div class="cart">
		<h1 className="name">Cart {this.state.currentCart.id}</h1>
				<ul>
		{this.state.currentCart.orderlines.map(function(orderline) {
		    return <ListItemWrapper key={orderline.id} data={orderline}/>;
		})}
		</ul>

		</div>
	);
    }
});
