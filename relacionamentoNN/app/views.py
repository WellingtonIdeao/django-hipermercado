from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from . models import *
# Create your views here.


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'marca', 'categoria']


def marca_list(request, template_name='marca/marca_list.html'):
    query = request.GET.get('busca')
    if query:
        marca = Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()
    return render(request, template_name, {'lista': marca})


def marca_new(request, template_name='marca/marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('marca_list')
    return render(request, template_name, {'form': form})


def marca_edit(request, pk, template_name='marca/marca_form.html'):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})


def marca_delete(request, pk, template_name='marca/marca_delete.html'):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, template_name, {'marca': marca})


def marca_produto_list(request, pk, template_name='marca/marca_produto_list.html'):
    produtos = Produto.objects.filter(marca=pk)
    return render(request, template_name, {'produtos': produtos})



def produto_list(request, template_name='produto/produto_list.html'):
    query = request.GET.get('busca')
    if query:
        produto = Produto.objects.filter(descricao__icontains=query)
    else:
        produto = Produto.objects.all()
    return render(request, template_name, {'lista': produto})


def produto_new(request, template_name='produto/produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, template_name, {'form': form})


def produto_edit(request, pk, template_name='produto/produto_form.html'):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form})


def produto_delete(request, pk, template_name='produto/produto_delete.html'):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, template_name, {'produto': produto})


def produto_profile(request, pk, template_name='produto/produto_show.html'):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, template_name, {'produto': produto})


def categoria_list(request, template_name='categoria/categoria_list.html'):
    query = request.GET.get('busca')
    if query:
        categoria = Categoria.objects.filter(nome__icontains=query)
    else:
        categoria = Categoria.objects.all()
    return render(request, template_name, {'lista': categoria})


def categoria_new(request, template_name='categoria/categoria_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, template_name, {'form': form})


def categoria_edit(request, pk, template_name='categoria/categoria_form.html'):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, template_name, {'form': form})


def categoria_delete(request, pk,
                     template_name='categoria/categoria_delete.html'):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, template_name, {'categoria': categoria})


def categoria_produto_list(request, pk,template_name='categoria/categoria_produto_list.html'):
    produtos = Produto.objects.filter(categoria=pk)
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, template_name,
                  {'produtos': produtos, 'categoria:': categoria})