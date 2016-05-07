# Modulo desde donde se llaman a los testCases
import DroneFramework.test.ejerciciosConMocks.clasesParaTestear as pruebaRm

def correrEjerciciosDeTestConMocks():
   print "Prueba clase RemovalService, metodo rm"
   prueba= pruebaRm.RemovalServiceTestCase('test_rm')
   prueba.test_rm()
   print "finalizo exitosamente la prueba: clase RemovalService, metodo rm"

   print "\n Prueba_1 clase UploadlService, metodo testado upload_complete con metodo Indira, que mockea la clase"
   prueba= pruebaRm.UploadServiceTestCase('test_uploadComplete')
   prueba.test_uploadComplete()
   print "finalizo exitosamente la prueba clase UploadService, llamada a removal_service.rm"

   print "\n Prueba_2 clase UploadlService, metodo testeado upload_complete con mocking del metodo rm"
   prueba= pruebaRm.UploadServiceTestCaseUsingMockDeObjects('test_upload_complete')
   prueba.test_upload_complete()
   print "finalizo exitosamente la prueba clase: UploadService, llamada removal_service.rm"

   print "\n Prueba_3 clase UploadlService, metodo testado upload_complete con mocking de la clase de rm"
   prueba= pruebaRm.UploadServiceTestCaseConInstanciaDelServicio('test_upload_complete')
   prueba.test_upload_complete()
   print "finalizo exitosamente la prueba clase: UploadService, llamada removal_service.rm"

