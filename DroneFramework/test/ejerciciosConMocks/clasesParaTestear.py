#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear import DummyClass
class DummyClassTest(unittest.TestCase):
    print 'hola1'
    m = mock.Mock()
    print(m.hell())
    print 'hola2'
    dummy_object = DummyClass()
    spy = mock.Mock(wraps=dummy_object)
    print(spy.hello())
    print 'hola3'

# Esta clase testea la función 'rm' que necesita el modulo os (sistema operativo)
# y además necesita el modulo path para ver si existe o no el archivo
#Tanto el os y path con mockeados
from DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear import rm
class RmTestCase(unittest.TestCase):
    #notar el orden de los parámetros: el módulo exterior primero, luego el más interno y así sucesivamente
    @mock.patch('DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear.os.path')
    @mock.patch('DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm("any_path")
        print "test ok:no ejecutó rm porque no encontró archivo para borrar"
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")
        # test ok: si el método rm llama a remove del os-
        mock_os.remove.assert_called_with("any path")
        print "test ok:no ejecutó rm porque no encontró archivo para borrar"

from DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear import RemovalService
class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear.os.path')
    @mock.patch('DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        referenceRmServicioClase = RemovalService()
        
        # set up the mock
        mock_path.isfile.return_value = False

        referenceRmServicioClase.rm("any_path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Error al borrar. El archivo no se encuentra.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        referenceRmServicioClase.rm("any path")
        mock_os.remove.assert_called_with("any path")

from DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear import UploadService

#Testeo de la clase UploadService como lo haría Indira: mockenado la clase RemovalService
class UploadServiceTestCase(unittest.TestCase):

    @mock.patch('DroneFramework.test.ejerciciosConMocks.clasesYMetodosATestear.RemovalService')
    def test_uploadComplete(self, mock_RemovalService):
        # Se instancia la clase upload con el mocking de la clase que contiene el rm: RemovalService
        refUploadServicioClase =UploadService(mock_RemovalService)
        refUploadServicioClase.upload_complete("any_path")

        # testea si se llama correctaente al revicio rm de removalService
        mock_RemovalService.rm.assert_called_with("any_path")

#Testeo de la clase UploadService, con el Mocking del método de una instancia : RemovalService.rm
# usando el método decorador de mock @mock.patch.object para métodos y propiedades
class UploadServiceTestCaseUsingMockDeObjects(unittest.TestCase):

    # Notar el parámetro autoespect que hace que el número de argumentos utilizados
    # en la llamada tb sean los que estamos utilizando
    @mock.patch.object(RemovalService, 'rm', autoespect=True)
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete, which should, in turn, call `rm`:

        reference.upload_complete("my uploaded file")

        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")

        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")

# Testeo de la clase UploadService creando una instancia Mock del servicio
class UploadServiceTestCaseConInstanciaDelServicio(unittest.TestCase):

    def test_upload_complete(self):
        # build our dependencies, con esto esta creando un mock de la clase q tiene el servicio
        mock_removal_service = mock.create_autospec(RemovalService)

        # se crea una instancia de la clase a testear con la clase a mockear
        reference = UploadService(mock_removal_service)

        # llama al metodo a testear:upload_complete, que llama al metodo `rm` de la clase mockeada
        reference.upload_complete("my uploaded file")

        # testea si el método rm es llamado cuando se ejecuto metodo upload_complete
        mock_removal_service.rm.assert_called_with("my uploaded file")




