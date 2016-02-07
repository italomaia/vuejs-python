VueListModel = Vue.extend
  ready: ->
    el = $ this.$el
    src = el.attr 'src'
    $.get(src).done (data) => this.$set('results', data)

$ -> $('[vue-list]').each ->
  new VueListModel el: this
