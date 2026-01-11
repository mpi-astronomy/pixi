#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* A simple C function that adds two doubles */
static PyObject *
fast_add(PyObject *self, PyObject *args)
{
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    return PyFloat_FromDouble(a + b);
}

/* Method registration */
static PyMethodDef Methods[] = {
    {"fast_add",  fast_add, METH_VARARGS, "Add two numbers in C."},
    {NULL, NULL, 0, NULL}
};

/* Module definition */
static struct PyModuleDef cexamplemodule = {
    PyModuleDef_HEAD_INIT,
    "cexample",
    "A C extension module for fast astronomy math.",
    -1,
    Methods
};

/* Module initialization */
PyMODINIT_FUNC
PyInit_cexample(void)
{
    return PyModule_Create(&cexamplemodule);
}
